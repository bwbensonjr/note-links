---
id: 1011
url: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-2260
title: Deprecation of Legacy Worksheets and Dashboards | Snowflake Documentation
domain: docs.snowflake.com
source_date: '2026-04-15'
tags:
- database
- devops
summary: Snowflake is deprecating Legacy Worksheets and Dashboards on June 22, 2026,
  replacing them with Workspaces for SQL editing and offering migration paths to Streamlit
  apps or third-party BI tools for dashboards. Users and administrators must migrate
  their worksheets and dashboards before the deadline, with self-service migration
  tools becoming available starting April 20, 2026. After June 22, 2026, Legacy Worksheets
  and Dashboards will be permanently removed from Snowsight and no longer accessible.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Deprecation of Legacy Worksheets and Dashboards | Snowflake Documentation

Deprecation of Legacy Worksheets and Dashboards[¶](#deprecation-of-legacy-worksheets-and-dashboards)
====================================================================================================

Snowflake is deprecating two legacy surfaces in Snowsight: **Legacy Worksheets** and
**Legacy Dashboards**.

* **Legacy Worksheets** are replaced by [Workspaces](/user-guide/ui-snowsight/workspaces), the modern SQL
  editing experience that supports file-and-folder organization, sharing, and Git integration.
* **Legacy Dashboards** are retired, with migration paths to Streamlit apps or third-party BI tools.

Important

On **June 22, 2026**, Legacy Worksheets and Dashboards will be permanently removed from
Snowsight. Migrate your worksheets and dashboards before this date.

Timeline[¶](#timeline)
----------------------

| Date | Worksheets | Dashboards |
| --- | --- | --- |
| **April 20, 2026** | Workspaces becomes universal and the default editor for all accounts. Workspaces can no longer be disabled. Account administrators can still temporarily revert to Legacy Worksheets as the default editor until June 22. Self-service worksheet migration tooling available.  Starting June 1, creation of new Legacy Worksheets is disabled. Users receive in-product announcements with reminders to migrate before June 22. | Creation of new dashboards is disabled across all accounts. |
| **June 22, 2026** | Legacy Worksheets UI fully removed from Snowsight. Remaining worksheets are automatically migrated to Workspaces files. | Legacy Dashboards UI fully removed from Snowsight. Dashboards are no longer accessible. |

Expand

Show lessSee more

Legacy Worksheets[¶](#legacy-worksheets)
----------------------------------------

Legacy Worksheets are replaced by [Workspaces](/user-guide/ui-snowsight/workspaces), a modern SQL editing
experience that supports file-and-folder organization, sharing, and Git integration. Most accounts are already
using Workspaces as their default editor.

For the previous behavior change that defaulted accounts to Workspaces, see
[Defaulting accounts from Worksheets to Workspaces](/release-notes/bcr-bundles/un-bundled/bcr-2117).

Before the change:
:   Legacy Worksheets is available as a SQL editing experience in Snowsight. Account administrators and
    individual users can revert from Workspaces to Legacy Worksheets as the default editor using the
    `USE_WORKSPACES_FOR_SQL` parameter or the corresponding controls in the Snowsight settings.

After the change:
:   Legacy Worksheets is removed from Snowsight.

    * **April 20, 2026**: Workspaces can no longer be disabled. The feature flag used to disable Workspaces
      (documented in [Disable Workspaces](/user-guide/ui-snowsight/workspaces#label-disable-personal-database)) is ignored. All remaining accounts
      are defaulted to Workspaces as the default SQL editor.

      Account administrators can still temporarily revert the default editor to Legacy Worksheets using the
      `USE_WORKSPACES_FOR_SQL` parameter:

      Copy codeExpand code block

      ```
      ALTER ACCOUNT SET USE_WORKSPACES_FOR_SQL = 'never';
      ```

      Show lessSee more

      Scroll to top

      This revert capability is available until June 22, 2026.
    * **June 22, 2026**: The Legacy Worksheets UI is permanently removed. All entry points to Legacy Worksheets
      are removed from Snowsight. Setting `USE_WORKSPACES_FOR_SQL` to `'never'` is no longer
      supported. Any remaining legacy worksheets are automatically migrated to Workspaces files.

### Shared worksheets[¶](#shared-worksheets)

Worksheets previously shared with other users remain accessible to all shared users from the Legacy Worksheets
section in the Workspaces sidebar.

When worksheets are automatically migrated to Workspaces files, a copy is created for each user who had access.
The shared status is not preserved after migration.

For ongoing collaboration, use [shared workspaces](/user-guide/ui-snowsight/workspaces-shared), which
allow teams to collaborate in dedicated spaces with role-based access control and a wiki-style draft and
publish model. Shared workspaces are the recommended replacement for shared worksheets.

Legacy Dashboards[¶](#legacy-dashboards)
----------------------------------------

Snowsight Dashboards are retired. Snowflake provides a Dashboard-to-Streamlit conversion tool to migrate
existing dashboards to Streamlit apps running natively on Snowflake. You can also migrate to any
third-party BI or visualization tool.

Before the change:
:   Snowsight Dashboards are available in Snowsight for creating and viewing dashboards.

After the change:
:   Snowsight Dashboards are removed from Snowsight.

    * **April 20, 2026**: Creation of new dashboards is disabled across all accounts. Any action that would
      create a new dashboard is blocked.
    * **June 22, 2026**: Dashboards are entirely removed from Snowsight. Existing dashboards are
      no longer accessible after this date.

### Dashboard migration options[¶](#dashboard-migration-options)

* **Streamlit**: Open any existing dashboard and select **Generate Streamlit app** to convert it to a
  Streamlit app running natively on Snowflake.
* **Third-party BI tools**: Migrate to any BI or visualization tool of your choice.

Important

Migrate your dashboards before **June 22, 2026**. After this date, dashboards are no longer accessible.

Actions required[¶](#actions-required)
--------------------------------------

### For Legacy Worksheets[¶](#for-legacy-worksheets)

1. **Verify Workspaces access**: Ensure your users can access
   [Workspaces](/user-guide/ui-snowsight/workspaces) and that it functions as expected for
   your workflows.
2. **Review existing worksheets**: Open the **Legacy Worksheets** section in the Workspaces sidebar to
   verify that your worksheets are accessible.
3. **Migrate worksheets to Workspaces files**: Before June 22, 2026, convert your worksheets to
   Workspaces files by dragging them into your workspace, or use the self-service bulk migration tool
   when it becomes available.
4. **Update automation or bookmarks**: If you have bookmarks, automation, or documentation that
   references Legacy Worksheets URLs or entry points, update them to use Workspaces.

### For Snowsight Dashboards[¶](#for-snowsight-dashboards)

1. **Migrate dashboards before June 22, 2026**: After this date, dashboards are no longer accessible.
2. **Use the conversion tool**: Open any dashboard and select **Generate Streamlit app** to convert it
   to a Streamlit app.
3. **Consider alternative tools such as Snowflake Intelligence**: You can also migrate to third-party BI or visualization tools.

Additional notes[¶](#additional-notes)
--------------------------------------

* **Temporary revert controls**: Between April 20 and June 22, 2026, account administrators can
  temporarily revert the default editor to Legacy Worksheets using the `USE_WORKSPACES_FOR_SQL`
  parameter. Individual users can also revert their own default. These controls are removed on June 22,
  2026. For details on these controls, see
  [Defaulting accounts from Worksheets to Workspaces](/release-notes/bcr-bundles/un-bundled/bcr-2117).

Change log[¶](#change-log)
--------------------------

| Update | Date |
| --- | --- |
| Initial publication | 23-Mar-26 |

Expand

Show lessSee more

Ref: 2260
