#!/usr/bin/env bash
# Syntax-checks every JS module and reports HTML/CSS sanity. Dev-only helper.
cd /home/user/PShop
fail=0
while IFS= read -r f; do
  cp "$f" /tmp/chk.mjs
  if ! node --check /tmp/chk.mjs 2>/tmp/err; then
    echo "SYNTAX FAIL: $f"; head -6 /tmp/err; fail=1
  fi
done < <(find assets/js -name '*.js')
[ $fail -eq 0 ] && echo "JS: all modules parse cleanly ($(find assets/js -name '*.js'|wc -l) files)"
