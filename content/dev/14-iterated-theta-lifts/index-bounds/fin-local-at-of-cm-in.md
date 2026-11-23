---
id: fin-local-at-of-cm-in
title: An integral frame at a finite place from a CM input
kind: theorem
decl: GlobalTheory.ArcCM.finLocalAt_of_cmIn
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.LocalArcIntegralityOfCmNormalisedTrivialisation
covers: 334
status: drafted
drafted_by: writer@claude
---
This theorem does the local work behind the finite-place bound of [`cfOf_fin_bound`](/entry/cf-of-fin-bound/). At a prime $w$ of $K_1$, it puts the evaluation of the arc datum into a frame where integral sections stay integral, with an explicit control of the denominators. It is used through its second name [`localArcIntegrality_of_cmNormalisedTrivialisation`](/entry/local-arc-integrality-of-cm-normalised-trivialisation/).

## Statement

Use $d$, $s$, $T$, $w$, $\lambda$, $e(w|\lambda)$ and $m_\lambda$ as in [`cfOf_fin_bound`](/entry/cf-of-fin-bound/). Assume `Known`, `ModelsAt Xo c` and `Std d`. Index the arc letters by $x = (\tau, k)$, with lines $\ell_x$. Then for every weight $(a', n)$ there are:

- a complete ultrametric field $\Omega$ with an embedding $\iota \colon K_1 \to \Omega$ and $0 < r < 1$ with $|\iota x| = r^{\operatorname{ord}_w x}$, a subfield $K_0$ with infinite residue field, and a set $S$ of elements of norm in $(0,1)$ whose norms are dense in $(0,1)$ (a `FinSite`);
- $\gamma \in \Omega^\times$ with $|\gamma| = r^{-\operatorname{ord}_w I_T}$, and $\lambda_x \in \Omega^\times$ with $|\lambda_x| = r^{-\operatorname{ord}_w I_{\ell_x}}$;
- matrices $A_\tau, B_\tau$ with $A_\tau B_\tau = 1$ and all entries of $A_\tau$ of norm at most $r^{-e(w|\lambda) m_\lambda}$,

such that the following holds. Let $F$ be a section of weight $(a', n)$ that is integral at $\lambda$. Let $P_j$ be the coefficient of $t^j$ of the polynomial of $F$ at the arc, mapped by $\iota$. Let $t \in S$ and let $Y = (Y_\tau)$ be matrices over $K_0$ with entries of norm at most $1$ and $|\prod_\tau \det Y_\tau| = 1$. Put $Y'_{\tau,i,k} = \lambda_{(\tau,k)}^{-1} (Y_\tau B_\tau)_{i,k}$. Then $P_j(Y') t^j \to 0$ as $|j| \to \infty$, and

$$\Bigl|\gamma^{-n} \sum_{j \in \mathbb{Z}} P_j(Y')\, t^j\Bigr| \le 1.$$

## Proof

1. **The completion.** `exists_finSite_norm_eq_zpow_siteAlg` gives a complete discrete valuation ring $V$ and $K_1 \to \operatorname{Frac} V$ that induces $\operatorname{ord}_w$. On $K = c.F$ the valuation is $e(w|\lambda) \operatorname{ord}_\lambda$.
2. **A model at $\lambda$.** Take a rational prime $p \in \lambda$ (`exists_prime_mem`). `exists_valuationSubring_complex_comap_val_eq` gives a valuation ring $W \subset \mathbb{C}$ that meets $K$ in the valuation ring of $\lambda$. `ModelsAt` gives a model over $W \cap K$. The structure maps lift to $V$ (`exists_lift`).
3. **An integral model of the arc.** `exists_arcIn_over_valuationRing` gives arcs over $V$ and over $\operatorname{Frac} V$. `exists_intModel_heq` gives an `IntModel`: a scalar $\gamma \neq 0$ that relates the theta section of $d$ to an integral theta section (`ThMul`), and matrices $g_\tau$ with nonzero determinant that express the letters of $d$ in an integral basis. `ArcGamma.vV_gamma` gives $v(\gamma) = -\operatorname{ord}_w I_T$.
4. **The letters.** For each letter $x$ choose $c_x \in K_1^\times$. If $s$ gives no abelian letter at $x$, take $c_x = 1$: `discr_mul_xi_integral` and `IntLetterCoord.main` show that $|d_E|\, g_{x,i}$ is integral. Otherwise take a local generator of the ideal of $\ell_x$ (`exists_locGen`): `abelian_letter_integral` shows that $n'\, c_x\, g_{x,i}$ is integral. In both cases `bound_of_mul_mem` gives $v(c_x\, g_{x,i}) \ge -e(w|\lambda) m_\lambda$.
5. `finLocalAt_of_intModel` gives the conclusion with $\lambda_x = c_x^{-1}$ and $A_\tau = \operatorname{diag}(c_\tau)\, g_\tau$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [LocalArcIntegralityOfCmNormalisedTrivialisation.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LocalArcIntegralityOfCmNormalisedTrivialisation.lean#L159). `FinLocalAt` is in [FinLocalCutAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/FinLocalCutAt.lean#L43). The helper lemmas `exists_intModel_heq`, `mem_range_of_le_one`, `exists_lift`, `bound_of_mul_mem`, `exists_prime_mem` and `exists_locGen` are in the same file, namespace `FinLoc`. `finLocalAt_of_intModel` is in [FinLocalAtOfIntModel.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/FinLocalAtOfIntModel.lean#L141).

- `Std d` is used only as `hS.1`, that is `d.OverBase`. This holds for every arc datum (`ArcDatum.overBase`), so the hypothesis `Std d` adds nothing here.
- We have not unfolded `IntModel` beyond its fields, nor the integrality lemmas of step 4.
