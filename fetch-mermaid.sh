#!/usr/bin/env sh
# Downloads the pinned Mermaid JS bundle for self-hosting.
# Run once after cloning, and again whenever you want to update the version.
#
# Why: MkDocs Material loads Mermaid from unpkg.com by default (no version pin,
#      external request on every page load). Adding the file locally and listing
#      it in extra_javascript makes Material skip the unpkg injection entirely.
#
# To update the version:
#   1. Change MERMAID_VERSION below
#   2. Run this script once (hash check will fail — expected)
#   3. Run: sha256sum docs/assets/javascripts/mermaid.min.js
#   4. Update MERMAID_SHA256 with the new hash, then re-run

MERMAID_VERSION="11.4.1"
# SHA-256 of mermaid@11.4.1/dist/mermaid.min.js from jsDelivr.
# Verify with: sha256sum docs/assets/javascripts/mermaid.min.js
MERMAID_SHA256="a43bc1afd446f9c4cc66ac5dd45d02e8d65e26fc5344ec0ef787f88d6ddb6f9e"
DEST="docs/assets/javascripts/mermaid.min.js"

mkdir -p "$(dirname "$DEST")"

curl -fsSL \
  "https://cdn.jsdelivr.net/npm/mermaid@${MERMAID_VERSION}/dist/mermaid.min.js" \
  -o "${DEST}"

# Verify integrity — abort and delete the file if the hash doesn't match
ACTUAL=$(sha256sum "${DEST}" | cut -d' ' -f1)
if [ "${ACTUAL}" != "${MERMAID_SHA256}" ]; then
  echo ""
  echo "ERROR: SHA256 mismatch for mermaid.min.js"
  echo "  Expected: ${MERMAID_SHA256}"
  echo "  Got:      ${ACTUAL}"
  rm -f "${DEST}"
  echo ""
  printf "Press any key to close..."
  if [ -t 0 ]; then
    old=$(stty -g)
    stty raw -echo
    dd bs=1 count=1 2>/dev/null
    stty "$old"
  fi
  echo ""
  exit 1
fi

echo ""
echo "Saved mermaid ${MERMAID_VERSION} -> ${DEST} (SHA256 verified)"
echo ""
printf "Press any key to close..."
if [ -t 0 ]; then
  old=$(stty -g)
  stty raw -echo
  dd bs=1 count=1 2>/dev/null
  stty "$old"
fi
echo ""
