# Project: Multi-POV Interactive Fiction Generator (CYOA)

## Objective
Build a Python-based generator that uses LLMs (with strict structured output via Pydantic) to adapt classic literature into multi-perspective Choose Your Own Adventure (CYOA) narratives, exporting directly to Twine/Twee format.

## Core Reference Text
- **Source:** *The Hound of the Baskervilles* by Sir Arthur Conan Doyle (Public Domain).
- **Playable POVs:**
  1. **Dr. John H. Watson:** Field observation, social trust, interviews at Baskerville Hall.
  2. **Sherlock Holmes:** Covert surveillance from the moor stone hut, deduction, chemical/trace analysis.
  3. **Jack Stapleton (Antagonist):** Mire navigation, deception, managing hound preparation without raising the suspicion threshold.

## Architecture & Constraints
1. **Model:** Web-and-Anchor Model. Multiple characters branch independently between shared canon anchor points (e.g., Arrival -> Night of Escaped Convict -> Merripit House Dinner).
2. **Graph Safety:** Graph generation uses breadth-first traversal with depth limits (`max_depth`) to prevent exponential combinatorial explosion.
3. **Validation:** NetworkX checks for dangling links, isolated nodes, and terminal state resolution before export.
4. **Target Export:** Standard Twee 3 (`.twee`) format readable by Twine/Tweego.