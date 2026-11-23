---
title: The local theory from the admitted inputs
decls:
  - Formalism.MainNotions.LiftingTheory.lifting_all_parts_of_admitted
  - Formalism.MainNotions.LiftingTheory.local_theory_of_admitted
  - Formalism.MainNotions.LiftingTheory.frobenius_lifting
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local theory from the admitted inputs

This section completes the proof of [the local theory](/entry/local-parts-of-admitted/) with the constants $(10, 23, 32, 32)$. It remains to prove the lifting statements 8(a), 8(b) and 8(e): lifting in cases A and B from the admitted inputs, and descent to a subfield by corestriction. The whole theory is then the conjunction of the two theorems. It is used in [the local constants from the admitted local Galois statements](/entry/local-constants-from-admitted-local-galois-statements-alt/), which passes the four constants to the global part of the proof.

We keep the notation of the previous section: the cases A and B, admissible maps $F \colon T_1 \to T_2$ for $(M, h)$, the exponents $e'_A$ and $e'_B$, the eight statements of the local theory, and the admitted inputs (A1) to (A23).

**Theorem 8.20.1 (Lifting from the admitted inputs).** Assume the admitted inputs. Then statement 8 of the local theory holds with $C_A = 23$ and $C_B = C_K = 32$.

Lean: `Formalism.MainNotions.LiftingTheory.lifting_all_parts_of_admitted`

*Proof.* Lifting in case B, 8(b), follows from (A1), (A2), (A5), (A6), (A11), (A13) to (A15), (A17) and (A21) to (A23), together with the killing by $p^{e_{WB}}$ of statement 2. Lifting in case A, 8(a), follows from (A2), (A5), (A6), (A9), (A13) to (A15), (A18), (A19) and (A21) to (A23), together with the killing by $p^{e_W}$. Statements 8(c) and 8(d) are proved in [the previous section](/entry/local-parts-of-admitted/). For 8(e), input (A20) gives a corestriction from the cohomology of the restricted lattices over $K$ to the cohomology over $K'$ that sends finite classes to finite classes, commutes with $F$, and satisfies $\mathrm{cor} \circ \mathrm{res} = g$; restriction keeps classes finite. Let $c$ be a finite cocycle of $T_2$ over $K'$, and $e$ the exponent of case A or B. By 8(a) or 8(b) over $K$, $p^e \operatorname{res} c$ is $F$ of a finite class plus a coboundary. Applying the corestriction, $g p^e c$ is $F$ of a finite class plus a coboundary. Write $g = p^{v_p(g)} m$ with $p \nmid m$; then $m$ is a unit of $\mathcal{O}$, so $F$ lifts with exponent $e + v_p(g)$. In case B with $s = 1$, $[K : K_0] = p - 1$, and $K_0 \subseteq K'$ makes $g$ a divisor of $p - 1$, so $v_\ell(g) = 0$. $\square$

**Theorem 8.20.2 (The local theory from the admitted inputs).** If the admitted inputs hold, then the local theory with constants $(10, 23, 32, 32)$ holds.

Lean: `Formalism.MainNotions.LiftingTheory.local_theory_of_admitted` (also `Formalism.MainNotions.LiftingTheory.frobenius_lifting`, the same statement as an implication).

*Proof.* Statements 1 to 7 are given by [Theorem 8.19.8](/entry/local-parts-of-admitted/) on the parts of the local theory, and statement 8 by the lifting theorem. $\square$

**Remark 8.20.3 (Formalization).** The three theorems are in [BaseChangePreservesUnitaryOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BaseChangePreservesUnitaryOf.lean#L4818), lines 4818 to 4841. The lifting step ignores (A3), (A4), (A7), (A8), (A10) and (A12). `local_parts_of_admitted` proves 8(c) and 8(d), and `local_theory_of_admitted` drops them and takes them again from `lifting_all_parts_of_admitted`. The name `frobenius_lifting` says less than the statement, which is the whole local theory. `local_theory_closed_form` (line 4843) puts the constants into the existential statement `RealisationStatementAll`. The namespace `CrystallineLiftingBounds` has second versions of `local_theory_of_admitted` and `frobenius_lifting` (lines 4856 and 4859) with the constants $(23, 32, 32)$, through `admitted_iff_base_admitted`, which is the identity. The descent step is `lifting_descent_to_subfields`; its proof through `coreDesc_of` was not opened, and the argument above uses only the three properties of the corestriction in (A20).

## Notes and references

The chapter feeds the local and global parts of the proof. The local Theorems B and C give [Theorem B of admitted inputs](/entry/theorem-b-of-admitted-inputs/) and [Theorem C of admitted inputs](/entry/theorem-c-of-admitted-inputs/). The arc lifting gives [the universal part in case A](/entry/universal-part-case-a/), and Theorem E with its corollary gives [the closing of Corollary A](/entry/thm-ecor-a-closing/). The export bound goes to [the main link for families](/entry/link-fam-main/), the integrality from the metric to [the integrality statement of the local Bloch-Kato chapter](/entry/integrality-from-metric-of-le/), the display bound to [normalized ring data](/entry/normalized-ring-data/), and the local theory of this section to [the local constants from the admitted local Galois statements](/entry/local-constants-from-admitted-local-galois-statements-alt/). The main difference from the classical sources below is that every bound here is explicit in the Hodge-Tate jumps.

- The groups $H^1_f$ of finite classes: S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift* I, Progr. Math. 86, Birkhäuser, 1990, §3.
- The period rings $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$: J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223 (1994), Exposé II.
- The Galois cohomology of $p$-adic fields: J.-P. Serre, *Galois Cohomology*, Springer, Chapter II, §5.
- Lattices in a representation with a reducible reduction, the model for the congruences of sections 17 and 18: K. Ribet, *A modular construction of unramified p-extensions of Q(μ_p)*, Invent. Math. 34 (1976), Proposition 2.1.
- Modules of finite length, for the colengths: M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969, Chapter 6.
