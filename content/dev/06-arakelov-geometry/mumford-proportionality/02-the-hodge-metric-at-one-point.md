---
title: The Hodge metric at one point
decls:
  - GlobalTheory.PointHodge.pointwise_hodge
  - GlobalTheory.HodgeRelation.chernTop_lieGram_rel_mul
  - GlobalTheory.T.hodgeMetric_chernDensity_lieGram_relation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge metric at one point

This section introduces the Hodge metric on the automorphic vector bundles of a unitary Shimura variety and proves that its Chern forms satisfy the Grassmann relations of [the compact dual](/entry/grass-top/) at each point. With the theorem on linear forms this gives the pointwise form of proportionality: at each point, the top Chern density of a polynomial $R$ is the flag degree times the density of the point polynomial. The section on [the Chern integrals of the Hodge metric](/entry/has-chern-integral-covol-flag-deg/) integrates this identity.

We keep the notation of the [first section](/entry/grass-top/): the CM field $E$, the embeddings $I = \operatorname{Hom}(E, \mathbb{C})$, the set $\Psi$, the signature $(p, q)$, $N = p + q$ and the ranks $m_\tau$.

**Definition 7.2.1 (Frames and Hermitian metrics).** Let $X$ be a variety of dimension $n$ over a field $F$ and $\sigma \colon F \to \mathbb{C}$ an embedding. Let $X(\mathbb{C})$ be the set of complex points of $X$ over $\sigma$, with the analytic topology ([complex manifolds](/learn/geometry/#complex-manifolds)). A *framed family of bundles* $\mathcal{E}$ of ranks $(m_\tau)_{\tau \in I}$ is given by a set $S(x)$ of *frames* at each point $x$ of $X$: each frame $A$ is a family of invertible matrices $A_\tau \in \mathrm{GL}_{m_\tau}(F(X))$ over the function field. Let $O \subseteq X$ be open. A *Hermitian metric* $h$ on $\mathcal{E}$ over $O$ gives, for each $y \in O(\mathbb{C})$, each frame $A \in S(y)$ and each $\tau$, a matrix $h_A(y)_\tau \in M_{m_\tau}(\mathbb{C})$ such that:

1. $h_A(y)_\tau$ is positive definite;
2. its real and imaginary parts are smooth functions of $y$;
3. for two frames $A, A' \in S(y)$, with $g = (A' A^{-1})(y)$, we have $h_{A'}(y)_\tau = g_\tau\, h_A(y)_\tau\, g_\tau^*$.

The rule 3 says that $h_A$ is the Gram matrix of one [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) on the fibre, read in the frame $A$. An *algebraic chart* at $y$ is a chart $\phi$ of $X(\mathbb{C})$ near $y$ with values in $\mathbb{C}^n$, given by algebraic functions. In such a chart and a frame $A$ we have the Gram family $w \mapsto h_A(\phi^{-1}(w))$, and so the top Chern density $\rho_R$ of the [first section](/entry/grass-top/).

**Definition 7.2.2 (Lie base and Hodge metric).** Let $Z$ be a moduli space of abelian varieties with $\mathcal{O}_E$-action of signature $(p, q)$, with a toroidal model; let $Z_\eta$ be its generic fibre and $B \subset Z_\eta$ its boundary ([toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications)). Let $\sigma$ be a complex embedding of the field of definition, with a uniformization datum $U$ of the components of $Z_\eta(\mathbb{C}) \setminus B$ ([the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization)). Let $Y_k$ be the variety of a toroidal flag space over one component $k$, with its map $\pi_k$ to $Z_\eta$ and its divisors $D_{\tau,i}$. A *Lie base* for $Y_k$ is a variety $X$, an open immersion $j \colon X \to Z_\eta$, a morphism $f \colon Y_k \to X$ with $j \circ f = \pi_k$, a framed family $\mathcal{E}$ on $X$ and a frame $A_0$, tied to a frame of the Lie algebra of the universal semi-abelian scheme at the generic point of $X$. Its *open part* is $O = j^{-1}(Z_\eta \setminus B)$. Over $O(\mathbb{C})$ the universal family is abelian, and $\mathcal{O}_E$ splits its Lie algebra into eigenspaces, one for each $\tau$. The *Hodge metric* $h$ on $\mathcal{E}$ over $O$ is the Gram matrix of the Hodge form (the polarization form of the uniformization, with the constant $2\pi$) in an eigenframe at $j(y)$ that matches the frame $A$.

The bundle $\mathcal{E}_\tau$ is the $\tau$-eigenspace of the Lie algebra, of rank $m_\tau$. So the Hodge metric is the metric of the automorphic bundles on the Shimura variety, in the sense of [Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem).

**Theorem 7.2.3 (Grassmann relations for the Hodge metric).** Let $X$, $j$, $f$, $\mathcal{E}$, $A_0$ be a Lie base for $Y_k$, with open part $O$ and Hodge metric $h$. Let $y \in O(\mathbb{C})$, let $\phi$ be an algebraic chart at $y$, let $A \in S(y)$, and put $G(w) = h_A(\phi^{-1}(w))$. Then for each $\tau \in \Psi$, each $k \geq 1$ and each $Q \in \mathbb{R}[c_{\tau,k}]$,
$$\rho_{r_{\tau,k} Q}(G)(\phi(y)) = 0, \qquad r_{\tau,k} = \sum_{a=0}^{k} (-1)^{k-a}\, c_{\tau,a}\, c_{\bar\tau,k-a}.$$

Lean: `GlobalTheory.HodgeRelation.chernTop_lieGram_rel_mul` (also `GlobalTheory.T.hodgeMetric_chernDensity_lieGram_relation`, a second name).

The hypotheses also include the two conditions on $\sigma$ and $U$ that every theorem of this chapter on the Hodge metric assumes; they are described in the Remark (Formalization).

*Proof.* First, $\dim X = |\Psi|\,pq$, the dimension of the symmetric domain. Fix an identification of the coordinates with $\Psi \times \{1..p\} \times \{1..q\}$. Let $\mathcal{D}$ be the bounded domain of matrices $z = (z_\tau)_{\tau \in \Psi}$ with $1 - z_\tau^* z_\tau$ positive definite, and let $M$ be the model Gram family on $\mathcal{D}$, built from the matrices $1 - z_\tau^* z_\tau$ and $1 - z_\tau z_\tau^*$. This is the Hodge metric of the universal family on $\mathcal{D}$, and it is smooth with invertible values.

1. *Local model.* Near $v = \phi(y)$ there are a holomorphic map $\psi$ into $\mathcal{D}$ and a holomorphic family $g$ of invertible matrices with $G = g\,(M \circ \psi)\,g^*$. This is the uniformization of $O(\mathbb{C})$ by $\mathcal{D}$, read in the chart.
2. *Frame change.* The Chern forms of a Hermitian metric do not change under a holomorphic change of frame: the curvature changes by conjugation. So $\rho_P(G)(v) = \rho_P(M \circ \psi)(v)$ for every $P$.
3. *Change of coordinates.* Under the holomorphic map $\psi$ a top form is multiplied by $|\det d\psi|^2$. So $\rho_P(M \circ \psi)(v) = |\det d\psi(v)|^2\, \rho_P(M)(\psi(v))$.
4. *Homogeneity.* The group of $\mathcal{D}$ acts transitively by fractional linear maps $z \mapsto (az + b)(cz + d)^{-1}$, and it preserves $M$ up to holomorphic frame change. So by steps 2 and 3 there is $\kappa$, depending on the point $\psi(v)$ but not on $P$, with $\rho_P(M)(\psi(v)) = \kappa\, \rho_P(M)(0)$.
5. *The origin.* At $z = 0$ the curvature of $M$ has constant coefficients in the coordinates, and the Chern forms of the rank $p$ and rank $q$ blocks satisfy $c(\mathcal{E}_\tau)\,c(\mathcal{E}_{\bar\tau}^\vee) = 1$ as forms. So $\rho_{r_{\tau,k} Q}(M)(0) = 0$.

Steps 2 to 5 give $\rho_{r_{\tau,k} Q}(G)(v) = |\det d\psi(v)|^2\,\kappa \cdot 0 = 0$. $\square$

**Theorem 7.2.4 (Pointwise proportionality).** Let $X$, $j$, $f$, $\mathcal{E}$, $A_0$ be a Lie base for $Y_k$, with open part $O$ and Hodge metric $h$. Let $\lambda$ be a weight and $R \in \mathbb{R}[c_{\tau,k}]$ with
$$\operatorname{antisym}(Q_{\lambda, \dim Y_k}) = \chi(R)\,\Delta.$$
Let $y \in O(\mathbb{C})$, let $\phi$ be an algebraic chart at $y$, let $A \in S(y)$ and $G(w) = h_A(\phi^{-1}(w))$. Then
$$\rho_R(G)(\phi(y)) = \deg_{\mathrm{Fl}}(\lambda)\, \rho_{P_0}(G)(\phi(y)).$$

Lean: `GlobalTheory.PointHodge.pointwise_hodge`.

*Proof.* The map $L(P) = \rho_P(G)(\phi(y))$ is linear in $P$, since substitution, the top coefficient and the real part are linear. The toroidal flag space has $\dim Y_k = |\Psi|\,N(N-1)/2$, and $|\Psi| = [E : \mathbb{Q}]/2$. We check the conditions of the [theorem on linear forms](/entry/grass-top/) with $n = \dim X$.

1. If $P$ is weighted homogeneous of degree $d$, then $P(c(G))$ is homogeneous of degree $d$ in the variables $x_{a,b}$, since $c_k$ has degree $k$. The top coefficient only sees degree $n$. So $L(P) = 0$ if $d \neq n$.
2. $c_0(G_\tau) = 1$, so $L((c_{\tau,0} - 1) Q) = 0$.
3. $c_k(G_\tau) = 0$ for $k > m_\tau$, since $\Theta_\tau$ is a matrix of size $m_\tau$. So $L(c_{\tau,k} Q) = 0$.
4. This is the [Grassmann relation for the Hodge metric](/entry/chern-top-lie-gram-rel-mul/).

The theorem on linear forms gives $L(R) = \deg_{\mathrm{Fl}}(\lambda)\, L(P_0)$. $\square$

**Remark 7.2.5.** In Mumford's proof the same identity comes from the compact dual: the Chern forms of the invariant metric on a Hermitian symmetric domain correspond, at each point, to the invariant forms of its compact dual (D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272). Here the identity is proved one point at a time, and only through the relations of the cohomology ring of the compact dual.

**Remark 7.2.6 (Formalization).** The theorems are in [PointwiseHodge.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PointwiseHodge.lean#L32) and [HodgeMetricChernDensityLieGramRelation.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricChernDensityLieGramRelation.lean#L20). Both assume the conditions `GoodEmb` on $\sigma$ and `IsUnf` on $U$, which we did not unfold. The tie of the Lie base to the generic eigenframe is the condition `Tied` of `IsLieBase`, which we did not unfold either. The Hodge metric is `lieGram` ([ExistsIsLieBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsLieBase.lean#L57)). It is defined as the transpose of the Hodge Gram matrix in a chosen eigenframe that matches $A$, and as $0$ when no such frame exists. The Hodge metric `hodgeMet` passes an arbitrary metric as a default argument (line 46), and the uniformization data for embeddings other than $\sigma$ are empty. The steps of the first proof are the lemmas `hodgeGram_localModel_algebraicChart_holomorphic`, `topChernDensity_invariant_holomorphic_frameChange`, `chernPolyTopDensity_comp_holomorphic_normSq_det`, `chernPolyTopDensity_boundedDomainModel_eq_mul_origin` and `chernPolyTopDensity_grassmannRelation_origin_zero`; we did not open their proofs, and the description of the model metric $M$ is from their names and from the domain of [the volume section](/entry/chern-top-domain/).
