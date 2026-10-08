# Document sources

These draft `document-source` records describe manuals, vendor pages and other
documents that cannot be pinned as Git source artifacts. They use the schema
from the exact core revision in `CORE_REVISION`.

Record the publisher, document version, access date, applicable model or family,
precise citation locations and rights. A `link-only` source has no recorded
content digest. `digest-recorded` identifies bytes inspected by the contributor;
it does not mean those bytes are archived or included in the bundle. URLs may
change in either case.

The [YRD210 Rev G manual record](yale-yrd210-manual-rev-g.json) follows a link
from Yale's official support directory. Its applicability is `family-context`:
the battery warning is documented, but the Zigbee raw attribute scale is not.
The PDF remains upstream; no PDF or page images are included here.

Use the [source contribution form](https://github.com/edgeloom-oss/edgeloom-catalog/issues/new?template=device-source.yml)
to suggest a document. Finding one useful source is a complete contribution;
you do not need to create a driver, mapping or bundle.
