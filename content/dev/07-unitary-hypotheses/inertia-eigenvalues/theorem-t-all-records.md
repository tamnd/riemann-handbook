---
id: theorem-t-all-records
title: The local lifting exponent for potentially crystalline lattices
kind: theorem
decl: GlobalTheory.InertiaEigenvalues.theoremT_all_records
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallinePeriodBoundAllConstantGeForty
covers: 3068
status: drafted
drafted_by: writer@claude
---
This theorem proves that a surjection of potentially crystalline lattices over $\mathbb{Q}_\ell$ is surjective on Bloch-Kato $H^1_f$ up to an explicit power of $\ell$, when $\ell$ is large. It assumes five published statements of $p$-adic Hodge theory and local Galois cohomology. Its only user is [its renaming](/entry/crystalline-period-bound-all-constant-ge-forty/), which goes to [the closing of the local inputs](/entry/closing-local-inputs-main-alt-alt/). The work is in [the lifting step](/entry/lifting-step-theorem-t-of-bhatt-scholze-fontaine/) and [its proof](/entry/theorem-tclosing-main/).

## Statement

Fix a prime $\ell$ and a finite extension $L$ of $\mathbb{Q}_\ell$ with ring of integers $\mathcal{O}$. Let $K'$ be a finite extension of $\mathbb{Q}_\ell$ such that $G_{K'}$ is normal of finite index in $G_{\mathbb{Q}_\ell}$, and such that $G_{\mathbb{Q}_\ell}$ maps the maximal unramified subfield $K'_0$ into itself inside $B$. Let $I \subseteq G_{\mathbb{Q}_\ell}$ be the subgroup that fixes $K'_0$ in $B$. Call a lattice $T$ in a representation $V$ of $G_{\mathbb{Q}_\ell}$ over $L$ *potentially crystalline* if $V|_{G_{K'}}$ is crystalline. For a finite set $\Sigma$ of characters $I \to L^\times$, say that *$I$ acts on $T$ through $\Sigma$* if each $\chi \in \Sigma$ is trivial on $G_{K'}$ and has order prime to $\ell$, and $D_{\mathrm{pcris}}(V)$ is the sum of the $\chi$-eigenspaces of $I$ for $\chi \in \Sigma$.

Let $\varphi \in G_{\mathbb{Q}_\ell}$ act on $K'_0$ as the Frobenius, and let $\Sigma$ be stable under conjugation by $\varphi$. For a character $\chi$ of $I$, let $o(\chi)$ be the least $k \ge 1$ with $\chi(\varphi^{-k} g \varphi^k) = \chi(g)$ for all $g \in I$, and let $r' = \max_{\chi_1, \chi_2 \in \Sigma} o(\chi_1 \chi_2^{-1})$.

**Theorem.** Assume `BhattScholzeIntegral`, `FontaineBcris`, `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`. Let $C \ge 40$ be an integer. Let $f \colon T_1 \to T_2$ be a map of potentially crystalline lattices that is onto on lattices. Let $N, \eta, H \in \mathbb{N}$ and $U \subset \mathbb{Z}$ finite. Suppose:

1. $1 \in \Sigma$, $\#\Sigma \le N$, $N \ge 2$, and $I$ acts on $T_1$ and on $T_2$ through $\Sigma$;
2. $0 \in U \subseteq [-\eta, H]$, $\#U \le N + 1$ and $1 \le \eta < H$;
3. the Hodge-Tate jumps of $T_1$ and of $T_2$ lie in $U$;
4. $C(HN^2 + N^3) < \ell$.

Then $4r' \le N^2$, and for each finite cocycle $c$ of $T_2$,

$$\ell^{\,C(Nr' + \eta(N + r'))}\, c \in f\bigl(Z^1_f(T_1)\bigr) + B^1(T_2).$$

Finite cocycles and $Z^1_f$ are defined in [the closing of the local bound](/entry/theorem-a-closing/).

## Proof

1. `GlobalTheory.T.bhattScholze_coefficients_of_padicInt_lattices` turns `BhattScholzeIntegral` (for $\mathbb{Z}_\ell$-lattices) into `BhattScholzeCrystallineLattices` (for $\mathcal{O}$-lattices).
2. `GlobalTheory.T.localLifting_admittedHypotheses_all` proves the six local inputs `Adm2` from `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`.
3. [The lifting step](/entry/lifting-step-theorem-t-of-bhatt-scholze-fontaine/) gives `Adm2 → Conclusion2 D C` from the two Bhatt-Scholze and Fontaine statements.

## In the Lean code

The theorem is at [CrystallinePeriodBoundAllConstantGeForty.lean line 13](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallinePeriodBoundAllConstantGeForty.lean#L13). The conclusion is `Conclusion2 D C`, which is `CorollaryALocal D.loc C`, which applies `thmT` to the data `pc` ([ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L178), lines 178 to 209). The definitions of potentially crystalline data are in [StatementPC.lean](lean:Formalism/WeaklyAdmissibleFiltrations/StatementPC.lean#L55).

- **Unused hypotheses.** The proof of the lifting step, `TheoremTClosing.main`, discards `Adm2` with `intro ... _`. So step 2 builds a proof that is never read. `BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK` and the datum `Cm` enter only through step 2. They are not needed for the conclusion.
- **Names.** The theorem is called Theorem T, its conclusion is `CorollaryALocal`, and the implication it uses is `HodgeTateFromSandwich`. The renaming speaks of a "crystalline period bound". None of these words name the statement, which is a lifting exponent for $H^1_f$.
- The data $HW$ and $F$ do not occur in the conclusion.
