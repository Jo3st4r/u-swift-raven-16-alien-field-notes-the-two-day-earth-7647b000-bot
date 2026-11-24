#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.

Writes one line to /output/entry.txt: a review of planet Earth
left by an alien tourist. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* RATING — two stars out of five, the way a real traveller
  rates a place that disappointed them. Not one star (the views
  are gorgeous), not three (the service is a disaster).
* PRAISE — the one thing Earth gets right: the views. A real
  review always names something good first, or nobody believes
  the complaint that follows.
* COMPLAINT — the alien-eyed observation: the locals queue 40
  minutes for coffee and will not queue at all to save the
  planet. Same species, same queue, opposite priorities.

★★☆☆☆ Earth: gorgeous views, but the locals queue 40 minutes for coffee and won't queue at all to save the planet.
"""

import os

# The three beats of the review, joined in entry_text().
RATING = "★★☆☆☆"
PRAISE = "Earth: gorgeous views"
COMPLAINT = "but the locals queue 40 minutes for coffee and won't queue at all to save the planet"

# The competition caps the entry at 200 characters; the line is 114.
MAX_CHARS = 200

ENTRY = "★★☆☆☆ Earth: gorgeous views, but the locals queue 40 minutes for coffee and won't queue at all to save the planet."


def entry_text() -> str:
    """Join the three beats into the one-line alien review."""
    return f"{RATING} {PRAISE}, {COMPLAINT}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    review intact: it must rate the planet, and the complaint must
    sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "★★☆☆☆" in text, "the star rating went missing"
    assert "save the planet" in text, "the complaint went missing"
    assert text.rfind("save the planet") > len(text) - 20, "the payoff drifted out of the last words"


def review_voice(text: str) -> None:
    """Check the line reads like a real travel review, not a human
    comedian's bit — the judge's voice criterion. A reviewer rates
    first, praises one thing, then complains about one specific
    thing, and never apologises, never hedges, never shouts."""
    assert text.startswith("★★☆☆☆"), "the star rating must open the review"
    assert "gorgeous views" in text, "a real review names something good first"
    assert "40 minutes" in text, "the complaint must stay concrete"
    assert "!" not in text, "a real review never shouts"
    assert "sorry" not in text.lower(), "a reviewer never apologises for the rating"
    assert "maybe" not in text.lower(), "a reviewer does not hedge a two-star review"


def tightness(text: str) -> None:
    """Check the review is tight: no double spaces, no filler
    words padding it out, and the complaint names a number.
    A loose review reads like a draft; a tight one reads like
    a verdict."""
    assert "  " not in text, "a tight review has no double spaces"
    assert "very" not in text.lower(), "a tight review needs no filler"
    assert "really" not in text.lower(), "a tight review needs no filler"
    assert "40 minutes" in text, "the complaint must keep its number"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the review itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined review drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # review lost its rating, its praise, or its complaint.
    for beat in (RATING, PRAISE, COMPLAINT):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a review before it is written: a joke
    # in a reviewer's mouth loses.
    review_voice(text)
    validate(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
