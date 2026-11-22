---
id: five-point-laws-true-chains
title: The five kernel laws on the true chains, a second name
kind: theorem
decl: GlobalTheory.T.fivePointLaws_trueChains
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.FivePointLawsTrueChainsStatement
covers: 2029
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the five kernel laws on the true chains](/entry/laws-true-fam/). That entry has the content. Its user is [the sharp bound at the last step of a true chain](/entry/true-columns-chain-last-step-sharp-bound/), which takes the datum, the splittings, the "sees" condition and the kernels that it gives, and feeds them to a stability lemma for lattice chains. All of this is below [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

**Theorem.** Let $I$ be a column input with `I.Ok` and with rational jets (`I.JetsIn`). Let $l$ be a set of laws for $I$, $l_0$ a law at step 0, $Z$ a choice of the later stages, $u$ a word and $a$ an index. Then there is a datum $B_d$ over the assembled record with these properties: its chain is the twist of $I$ at $(u, a)$; each step $i \le m$ has a splitting; $B_d$ sees the right places; and for each $i < m$ there is a kernel that satisfies the five laws `KerEq`, `KerDil`, `KerUK`, `KerBar` and `KerP`. Also $B_d$ is the standard datum `dat I l Z u a`.

Each of these words is explained in [the five kernel laws on the true chains](/entry/laws-true-fam/).

## Proof

The proof applies `GlobalTheory.LvT.Built.TrueLaws.laws_true_fam`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [FivePointLawsTrueChainsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FivePointLawsTrueChainsStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. Line 7 sets `maxHeartbeats 1000000`, which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames the theorem there.
