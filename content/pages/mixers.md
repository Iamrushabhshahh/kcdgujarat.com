---
# ─── Community Mixers ─────────────────────────────────────────────────────────
# Informal gatherings that run alongside the conference. These are NOT sessions
# and NOT timeline rows — a mixer has no slot in the printed schedule, so it
# lives here rather than in content/sessions or event.md's `timeline`.
#
# The homepage section renders only while this list has a published entry, so
# emptying the list (or `render: false` on every mixer) hides it completely —
# there is no separate flag to remember.
#
#   name        Card heading (required).
#   description One-line "who is this for".
#   when        Free text, e.g. "14:30 – 14:55". Omit if not fixed yet.
#   where       Room or area. Omit if not fixed yet.
#   activities  Bullet list on the card.
#   image       Card banner, 1200x630, under public/images/mixers/. The
#               filename carries a content hash, so a redrawn banner means a
#               new filename here too. Regenerate ours with
#               `python3 scripts/generate-mixer-art.py out.svg`.
#   imageAlt    Only set this when the art says something the title and
#               bullets don't — otherwise the card marks it decorative.
#   rsvpUrl     Only set this if a mixer needs its own sign-up. Ours don't —
#               they are open to every registered attendee, so the card shows
#               an "included with your ticket" note instead of a CTA.
#   inviteOnly  true renders an "Invite only" chip in place of any CTA.
#   accent      pink | blue | green — tints the card header and bullets.
#   order       Ascending. Ties break on name.
#   render      false hides one mixer.
eyebrow: "Community Events"
title: "Community Mixers"
description: "Informal gatherings running alongside KCD Gujarat 2026. Open to every registered attendee — no separate sign-up."
footnote: "Mixers are included with your KCD Gujarat 2026 ticket. Just turn up — there is no separate RSVP."

mixers:
  - name: "Women in Cloud Native Mixer"
    description: "An exclusive gathering for women in the cloud-native community."
    when: "14:30 – 14:55"
    where: "Cafe Beans (First Floor)"
    image: "/images/mixers/women-in-cloud-native-f071f6e2.svg"
    activities:
      - "Casual networking across DevOps, SRE, and Platform Engineering"
      - "BoF discussions on careers, growth, and leadership"
      - "Light snacks, refreshments & special goodies"
      - "Fun photo session & networking moments"
    accent: "pink"
    order: 10
---
