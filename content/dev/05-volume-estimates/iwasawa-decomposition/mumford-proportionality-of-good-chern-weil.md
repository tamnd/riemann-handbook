---
id: mumford-proportionality-of-good-chern-weil
title: Mumford proportionality from good Chern-Weil theory
kind: theorem
decl: GlobalTheory.Proportionality.mumfordProportionality_of_goodChernWeil
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ToroidalFlagProportionalityOfGoodChernWeil
covers: 1340
status: drafted
drafted_by: writer@claude
---
This theorem proves a form of Hirzebruch-Mumford proportionality for toroidal flag spaces: the top self-intersection of an automorphic line bundle is a covolume times a flag degree. The analytic work is in [the good base](/entry/exists-good-base/). Its [restatement](/entry/toroidal-flag-proportionality-of-good-chern-weil/) is applied to the field `p16` of the bundle of [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/), which is proved by [`goodChernWeil`](/entry/good-chern-weil/).

## Statement

**Chern integrals.** Let $X$ be a smooth projective variety over $F$, with $\sigma \colon F \to \mathbb{C}$, $\mathcal{E}$ a family of vector bundles $\mathcal{E}_\tau$ of ranks $m_\tau$, and $h$ a Hermitian metric on $\mathcal{E}$ over an open $O$. For a real polynomial $R$ in the Chern classes $c_j(\mathcal{E}_\tau)$, write $\int_O R = t$ when the Chern form $R(h)$ has positive and negative parts of finite mass on $O(\mathbb{C})$ and signed integral $t$ (`HasChernIntegral`). The metric is *good* (`IsGood`) when near each boundary point $X \setminus O$ is a union of coordinate hyperplanes of a chart, and $h$, $\det h^{-1}$, the connection and the curvature satisfy growth bounds (`GoodBound`). These are the good metrics of Mumford, "Hirzebruch's proportionality theorem in the non-compact case" (Invent. Math. 42, 1977).

**Flags.** Let $f \colon Y \to X$ carry a full flag of each $\mathcal{E}_\tau$ (`Refines`), with divisors $D_{\tau,i}$ for the graded line bundles (`IsGraded`). For a polynomial $Q$ in variables $x_{\tau,i}$, let $I(Q)$ be the linear map with $I(\prod_k x_{s(k)}) = (D_{s(1)} \cdots D_{s(d)})_Y$, $d = \dim Y$ (`interPoly`). Let $R(e)$ put the elementary symmetric polynomials of $x_{\tau,0}, \dots, x_{\tau,m_\tau-1}$ in place of the $c_j(\mathcal{E}_\tau)$, let $P = \prod_{\tau,i} (-x_{\tau,i})^{m_\tau-1-i}$ and $\Delta = \prod_\tau \prod_{i<j}(x_{\tau,j} - x_{\tau,i})$.

**The hypothesis.** $\mathrm{GoodChernWeil}$ is the conjunction of:

1. (`GoodChernNumbers`) for a good metric, $\int_O R = I(R(e)\,P)$;
2. (`FlagPushForward`) if $\sum_{w \in \prod_\tau S_{m_\tau}} \operatorname{sgn}(w)\, wQ = R(e)\,\Delta$, then $I(Q) = I(R(e)\,P)$.

**The conclusion.** Fix a CM field $E$, a Hermitian $\mathcal{O}_E$-lattice of signature $(p,q)$, $N = p+q$, a moduli space with a toroidal model, $\sigma$ with `GoodEmb`, and components $U$ with `IsUnf`. Let $\Phi$ be a toroidal flag space: for each component $k$ a smooth projective variety $Y_k$ with divisors $D_{\tau,i}$. Let $\Psi$ be the set of embeddings $\tau$ with $\tau(r) = r_0$ (`Psi`). Let $\lambda \colon \Psi \times \{0,\dots,N-1\} \to \mathbb{Z}$ and $L_\lambda = -\sum_{\tau,i} e_\lambda(\tau,i) D_{\tau,i}$, with the exponents $e_\lambda$ of `exOf`. Then

$$(L_\lambda^{\dim Y_k})_{Y_k} = \operatorname{covol}(U_k) \cdot \deg_{\mathrm{Fl}}(\lambda).$$

Here $\operatorname{covol}(U_k)$ is a constant $c_N^{|\Psi|}$ times the measure of a fundamental set ([FirstIndexEqOfUnfolded.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/FirstIndexEqOfUnfolded.lean#L89)). With $D = |\Psi| \binom{N}{2}$ and $\ell_\lambda = -\sum_{\tau,i} \lambda_{\tau,i} x_{\tau,i}$,

$$\deg_{\mathrm{Fl}}(\lambda) = (-1)^D \sum_{w \in S_N^{\Psi}} \prod_\tau \operatorname{sgn}(w_\tau) \,\bigl[\textstyle\prod_{\tau,i} x_{\tau,i}^{N-1-w_\tau(i)}\bigr]\, \ell_\lambda^D.$$

## Proof

For fixed $k$ and $\lambda$, let $Q_\lambda = \bigl(-\sum_{\tau,i} e_\lambda(\tau,i)\, x_{\tau,i}\bigr)^{\dim Y_k}$.

1. [`exists_goodBase`](/entry/exists-good-base/) gives $f \colon Y_k \to X$, a bundle $\mathcal{E}$ whose flag on $Y_k$ is graded by the $D_{\tau,i}$, a good metric on an open $O$, and $\int_O R = \operatorname{covol}(U_k)\deg_{\mathrm{Fl}}(\lambda)$ for each $R$ with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$.
2. `antisymm_eq_chernRoots_mul_rootDiscr` gives such an $R$: an antisymmetrization is $\Delta$ times a block-symmetric polynomial.
3. `selfInter_Lw_interPoly`: $(L_\lambda^{\dim Y_k}) = I(Q_\lambda)$.
4. `GoodChernWeil.flag` combines the two parts of the hypothesis: $\int_O R = I(Q_\lambda)$.
5. `hasChernIntegral_unique`: a Chern integral has one value.

## In the Lean code

The theorem is in [ToroidalFlagProportionalityOfGoodChernWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ToroidalFlagProportionalityOfGoodChernWeil.lean#L19). The statements are in [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L30), the analytic definitions in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L124).

`GoodEmb` and `IsUnf` go only to `exists_goodBase`. The proof ends with `convert … <;> exact Subsingleton.elim _ _`; we have not checked which terms differ. We have not checked that $\deg_{\mathrm{Fl}}$ is a degree on $\prod_\Psi \mathrm{Fl}(N)$. The proposition `FlagDegFormula` ([FlagDegFormula.lean](lean:Formalism/DegreeFormula/FlagDegFormula.lean#L27)) says it is $D!\prod_\tau\prod_{i<j}(\lambda_{\tau,i} - \lambda_{\tau,j})/(j-i)$.
