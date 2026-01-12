"""Flask route handlers."""

from datetime import date

from flask import Blueprint, abort, current_app, render_template, request

bp = Blueprint("main", __name__)


def get_db():
    """Get database instance from app config."""
    return current_app.config["DATABASE"]


@bp.route("/")
def index():
    """Dashboard with stats and recent links."""
    db = get_db()
    stats = db.get_stats()
    recent = db.get_recent_links(limit=10)
    tags = db.get_all_tags()[:10]

    # Get tags for recent links
    link_tags = {}
    for link in recent:
        link_tags[link.id] = db.get_tags_for_link(link.id)

    return render_template(
        "index.html",
        stats=stats,
        recent=recent,
        top_tags=tags,
        link_tags=link_tags,
    )


@bp.route("/search")
def search():
    """Full-text search."""
    db = get_db()
    query = request.args.get("q", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 25

    if query:
        results = db.search(query, limit=100)
        # Manual pagination for search results
        total = len(results)
        start = (page - 1) * per_page
        end = start + per_page
        results = results[start:end]
    else:
        results = []
        total = 0

    # Get tags for results
    link_tags = {}
    for link in results:
        link_tags[link.id] = db.get_tags_for_link(link.id)

    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "search.html",
        query=query,
        results=results,
        link_tags=link_tags,
        page=page,
        total=total,
        total_pages=total_pages,
    )


@bp.route("/browse")
def browse():
    """Browse links with filters."""
    db = get_db()

    # Get filter parameters
    page = request.args.get("page", 1, type=int)
    sort = request.args.get("sort", "date_desc")
    selected_tags = request.args.getlist("tag")  # Multiple tags supported
    domain = request.args.get("domain")
    date_from_str = request.args.get("date_from")
    date_to_str = request.args.get("date_to")

    # Parse dates
    date_from = date.fromisoformat(date_from_str) if date_from_str else None
    date_to = date.fromisoformat(date_to_str) if date_to_str else None

    per_page = 25
    links, total = db.get_links_paginated(
        page=page,
        per_page=per_page,
        sort_by=sort,
        tags=selected_tags if selected_tags else None,
        domain=domain,
        date_from=date_from,
        date_to=date_to,
    )

    # Get tags for links
    link_tags = {}
    for link in links:
        link_tags[link.id] = db.get_tags_for_link(link.id)

    total_pages = (total + per_page - 1) // per_page

    # Get filter options
    all_tags = sorted(db.get_all_tags(), key=lambda t: t[0].lower())  # Sort alphabetically
    all_domains = db.get_all_domains()[:20]

    return render_template(
        "browse.html",
        links=links,
        link_tags=link_tags,
        page=page,
        total=total,
        total_pages=total_pages,
        sort=sort,
        selected_tags=selected_tags,
        domain=domain,
        date_from=date_from_str,
        date_to=date_to_str,
        all_tags=all_tags,
        all_domains=all_domains,
    )


@bp.route("/browse/tags")
def browse_tags():
    """View all tags."""
    db = get_db()
    tags = db.get_all_tags()

    # Group by category
    by_category: dict[str, list] = {}
    for name, category, count in tags:
        if category not in by_category:
            by_category[category] = []
        by_category[category].append((name, count))

    return render_template("tags.html", tags=tags, by_category=by_category)


@bp.route("/browse/dates")
def browse_dates():
    """View links grouped by date."""
    db = get_db()
    date_counts = db.get_date_counts()

    return render_template("dates.html", date_counts=date_counts)


@bp.route("/link/<int:link_id>")
def link_detail(link_id: int):
    """Single link detail view."""
    db = get_db()
    link = db.get_link_by_id(link_id)

    if not link:
        abort(404)

    tags = db.get_tags_for_link(link_id)

    return render_template("link.html", link=link, tags=tags)
