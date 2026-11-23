---
id: pointwise-hodge
title: Chern forms of the Hodge metric at one point
kind: theorem
decl: GlobalTheory.PointHodge.pointwise_hodge
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PointwiseHodge
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem is the pointwise half of [the Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/). At each point of the open part of a Lie base, the top Chern density of a polynomial $R$ with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$ is $\deg_{\mathrm{Fl}}(\lambda)$ times the top density of the point polynomial $P_0$. The parent entry integrates this identity against [the integral of $P_0$](/entry/has-chern-integral-point-poly-covol/). The proof is algebra: a linear form on Chern polynomials that satisfies four relations is fixed by its value on $P_0$.

## Statement

Use the setting and notation of [the Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/). For a polynomial $P$ in the variables $c_j(\mathcal{E}_\tau)$, a chart $\phi$ at a point $y$ of $O(\mathbb{C})$ and a frame $A$ at $y$, let $\rho_P(y)$ be the top density `chernTop`: put the Chern forms of the curvature of $h_A$ (the matrices `lieGram` in the frame $A$, read in the chart) into $P$, with a variable $x_{a,b}$ for $dz_a \wedge d\bar z_b$. Take the top coefficient `topCoeff`, the signed sum over permutations $w$ of the coefficients of $\prod_a x_{a,w(a)}$, and multiply its real part by $\pi^{-\dim X}$.

**Theorem.** Assume `GoodEmb` and `IsUnf`. Let $\lambda$ be a weight and $R$ a real polynomial with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$. Then for each $y \in O(\mathbb{C})$, each chart $\phi$ at $y$ and each frame $A$ at $y$,

$$\rho_R(y) = \deg_{\mathrm{Fl}}(\lambda)\,\rho_{P_0}(y).$$

## Proof

Fix $y$, $\phi$ and $A$. The map $L \colon P \mapsto \rho_P(y)$ is linear (`chernLin`, from `chernTop_add` and `chernTop_smul`).

1. `Φ.dim_eq` and `card_cmTypeEmbeddingsFixingRoot_eq_half_finrank` give $\dim Y_k = |\Psi| \cdot N(N-1)/2$, with $|\Psi| = [E:\mathbb{Q}]/2$.
2. `compactDual_linearForm_flagDegree_pointClass` is an algebraic statement. Let $L$ be a linear form on $\mathbb{R}[c_{\tau,k}]$, with $c_{\tau,k}$ of weight $k$, such that:
   1. $L(Q) = 0$ for $Q$ of weighted degree $\ne \dim X$;
   2. $L\bigl((c_{\tau,0} - 1)Q\bigr) = 0$;
   3. $L(c_{\tau,k}Q) = 0$ for $k > m_\tau$;
   4. for $\tau \in \Psi$ and $k \ge 1$, $L\bigl(\sum_{a=0}^{k} (-1)^{k-a} c_{\tau,a}\, c_{\bar\tau,k-a}\, Q\bigr) = 0$.

   Then $L(R) = \deg_{\mathrm{Fl}}(\lambda)\,L(P_0)$ for each $R$ as in the theorem.
3. Conditions 1 to 3 hold for the Chern forms of any metric: `chernPolyTopDensity_eq_zero_of_weightedDegree_ne_dim` and `chernPolyTopDensity_unit_and_above_rank`.
4. Condition 4 is the input of the Hodge metric: `hodgeMetric_chernDensity_lieGram_relation`.

Since $c_j(\mathcal{E}^\vee) = (-1)^j c_j(\mathcal{E})$, condition 4 says that the total Chern form of $\mathcal{E}_\tau \oplus \mathcal{E}_{\bar\tau}^\vee$ is $1$ in positive degree, after multiplication by any $Q$. The ranks $m_\tau + m_{\bar\tau}$ add up to $N$. On a Grassmannian the tautological subbundle $S$ and quotient bundle $Q$ satisfy $c(S)\,c(Q) = 1$ by the Whitney sum formula, since $S \oplus Q$ is trivial (Milnor and Stasheff, *Characteristic Classes*, §14). So conditions 1 to 4 copy the relations of the cohomology of a product of Grassmannians, the compact dual named in step 2.

## In the Lean code

The theorem is in [PointwiseHodge.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PointwiseHodge.lean#L32). The lemmas are second names:

- `GlobalTheory.T.compactDual_linearForm_flagDegree_pointClass` restates `GlobalTheory.GrassTop.grass_top`.
- `GlobalTheory.T.chernPolyTopDensity_eq_zero_of_weightedDegree_ne_dim` restates `GlobalTheory.GoodMetric.chernTop_eq_zero_of_weightedHomogeneous`.
- `GlobalTheory.T.chernPolyTopDensity_unit_and_above_rank` restates `GlobalTheory.GoodMetric.chernTop_unit`.
- `GlobalTheory.T.hodgeMetric_chernDensity_lieGram_relation` restates `GlobalTheory.HodgeRelation.chernTop_lieGram_rel_mul`.
- `GlobalTheory.T.card_cmTypeEmbeddingsFixingRoot_eq_half_finrank` restates `GlobalTheory.CMTypeCard.card_psi_eq_half`.

We have not unfolded `grass_top` or `chernTop_lieGram_rel_mul`. The conjugate embedding is `conjEmb` $= \overline{\phantom{x}} \circ \tau$ ([FlagBasis.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/FlagBasis.lean#L78)). The theorem does not relate $\dim X$ to $\dim Y_k$. If the weighted degree of $R$ and $P_0$ is not $\dim X$, then both sides are $0$ by condition 1, and the identity is true but empty.
