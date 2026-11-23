---
title: The decomposition on an snc atlas
decls:
  - GlobalTheory.LogDR.decomp_of_isLifted
  - GlobalTheory.T.frobenius_decomposition_of_lift
  - GlobalTheory.LogAtlas.exists_atlas_decomp
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The decomposition on an snc atlas

This section applies the splitting of [Theorem 9.1.7](/entry/di-decomp-of-is-lifted/) to a smooth projective variety $X$ over $\mathbb{F}_p$ with a divisor with simple normal crossings, when $X$ and the divisor lift to $\mathbb{Z}/p^2$. The result, [Theorem 9.2.5](/entry/exists-atlas-decomp/), gives a finite affine cover of $X$ on which Čech cohomology of twisted logarithmic forms is controlled by the hypercohomology of a de Rham complex with a larger twist. Section 3 uses it to prove vanishing.

We first define the divisors and covers. Let $R$ be a ring and $f : X \to \operatorname{Spec} R$ a scheme over $R$. Functions $t_1, \dots, t_d$ on an affine open $U \subseteq X$ are *étale coordinates* if the map $R[T_1, \dots, T_d] \to \mathcal{O}(U)$, $T_l \mapsto t_l$, is [étale](/learn/commutative-algebra/#flat-and-tale-algebras).

**Definition 9.2.1 (Relative snc family).** Let $f : X \to \operatorname{Spec} R$, $d \geq 0$, and let $L_1, \dots, L_s$ be line bundles on $X$ with sections $\sigma_1, \dots, \sigma_s$. The family $(L_i, \sigma_i)$ is a *relative snc family of dimension $d$* if each point of $X$ lies in an affine open $U$ with the following data: étale coordinates $t_1, \dots, t_d$ on $U$, a trivialization of each $L_i$ on $U$, and a map $e$ from $\{1, \dots, s\}$ to $\{1, \dots, d\} \cup \{\ast\}$, injective on the indices $i$ with $e(i) \neq \ast$, such that in the trivializations
$$\sigma_i = u_i\, t_{e(i)} \text{ if } e(i) \neq \ast, \qquad \sigma_i = u_i \text{ if } e(i) = \ast,$$
with $u_i$ a unit on $U$. We call $U$ with these data an *snc chart*.

So $X$ is smooth of relative dimension $d$ over $R$, each divisor $\sigma_i = 0$ is smooth over $R$, and distinct divisors meet transversally over $R$. A divisor $\sigma_i = 0$ can be empty on a chart, but two of them are never given by the same coordinate.

**Definition 9.2.2 (Snc atlas).** Let $X$ be integral with function field $K$ and $(E_c)_{c \in C}$ a finite family of Cartier divisors, with union of supports $Z$. An *snc atlas* of $(E_c)$ of dimension $n$, indexed by a totally ordered set $\iota$, consists of affine opens $U_i$ that contain the generic point and cover $X$, systems $x_i = (x_{i,1}, \dots, x_{i,n})$ of coordinates in $K^\times$, and subsets $J_i \subseteq \{1, \dots, n\}$, such that for each $i$:

1. at each $y \in U_i$, the $x_{i,l}$ lie in $\mathcal{O}_{X,y}$ and $d$ of each element of $\mathcal{O}_{X,y}$ is an $\mathcal{O}_{X,y}$-linear combination of the $dx_{i,l}$;
2. at each $y \in U_i$, the log units along $Z$ at $y$ are the elements $u \prod_{j \in J_i} x_{i,j}^{m_j}$ with $u$ a unit at $y$ and $m_j \in \mathbb{Z}$;
3. there is an injective partial map $e_i : C \to \{1, \dots, n\}$ with image $J_i$ such that at each $y \in U_i$, $E_c$ has the local equation $x_{i, e_i(c)}$ if $e_i(c)$ is defined and $1$ otherwise.

Condition 1 also asks a root condition on the chart, which we do not need below. The atlas is the algebraic form of a cover of $X$ by charts in which $Z$ is a union of coordinate hyperplanes.

**Definition 9.2.3 (Decomposition property).** Let $X$ be integral with function field of characteristic $p$, and let $\mathcal{A}$ be an snc atlas of $(E_c)_{c \in C}$. Write $\Omega^a_Z(G)$ for the logarithmic forms along $Z = \bigcup_c \operatorname{supp} E_c$ ([Definition 9.1.7](/entry/di-decomp-of-is-lifted/) of Section 1) and use the Čech complexes of the cover $(U_i)$. The atlas has the *decomposition property* if for each Cartier divisor $G$, each family of integers $0 \leq r_c < p$ and all $a, b \geq 0$:
$$\mathbb{H}^{a+b}\Big(\Omega^\bullet_Z\big(pG + \textstyle\sum_c r_c E_c\big)\Big) = 0 \implies \check H^b\big(\Omega^a_Z(G)\big) = 0.$$

**Theorem 9.2.4 (Decomposition from a Frobenius lift).** Let $X$ be integral with function field of characteristic $p$ and $\mathcal{A}$ an snc atlas of $(E_c)$ of dimension $n < p$. Assume that $Z$, the open sets $U_i$ and the coordinates $x_i$ of $\mathcal{A}$ have a Frobenius lift. Then $\mathcal{A}$ has the decomposition property.

Lean: `GlobalTheory.LogDR.decomp_of_isLifted` (also `GlobalTheory.T.frobenius_decomposition_of_lift`, a second name).

*Proof.* Fix $G$ and $0 \leq r_c < p$, and put $H = pG + \sum_c r_c E_c$. We apply [Theorem 9.1.7](/entry/di-decomp-of-is-lifted/) with $W_s = \bigcap_{i \in s} U_i$. The open sets contain the generic point, and the $x_i$ are systems of coordinates by condition 1 of the atlas. The divisor $H - pG = \sum_c r_c E_c$ is effective. Three lemmas on the atlas give the other hypotheses; each needs $r_c < p$.

1. On $U_i$, if $t$ is a local equation of $G$ at $y$, then $H$ has the local equation $t^p \prod_{j \in J_i} x_{i,j}^{\rho_j}$ with $0 \leq \rho_j < p$.
2. The exterior derivative maps $\Omega^q_Z(H)(W)$ into $\Omega^{q+1}_Z(H)(W)$ for each open $W$. A section of $\mathcal{O}_X(H)$ at $y$ is $h^{-1}$ times a regular function, with $h$ a local equation, and $d(t^{-p} \prod_j x_j^{-\rho_j} \omega) = t^{-p} \prod_j x_j^{-\rho_j} (d\omega - \sum_j \rho_j \operatorname{dlog} x_j \wedge \omega)$, since $d(t^p) = 0$.
3. For each $s$ and $j \in s$, each Cartier map for $x_j$ induces an isomorphism from $\Omega^\bullet_Z(G)(W_s)$ to the cohomology of $\Omega^\bullet_Z(H)(W_s)$. This is the Cartier isomorphism with a twist. In a chart, a form with the factor $x_j^{-\rho_j}$, $0 < \rho_j < p$, contributes nothing to the cohomology, because $\rho_j$ is a unit modulo $p$ in the formula of item 2.

So all hypotheses hold, and the theorem of Section 1 gives the implication. $\square$

The next theorem builds an atlas with a Frobenius lift from a lift of $X$ to $\mathbb{Z}/p^2$. Let $c : \mathbb{Z}/p^2 \to \mathbb{F}_p$ be the reduction map.

**Theorem 9.2.5 (Atlas with the decomposition property).** Let $p$ be a prime, $g : Y \to \operatorname{Spec} \mathbb{Z}/p^2$ a scheme, and $X = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p$ with projections $\pi : X \to Y$ and $f : X \to \operatorname{Spec} \mathbb{F}_p$. Assume that $X$ is integral, smooth of relative dimension $d$ and projective over $\mathbb{F}_p$, and $d < p$. Let $(L_i, \sigma_i)_{i \le s}$ be a relative snc family of dimension $d$ on $Y$ over $\mathbb{Z}/p^2$. Then there are an integer $m$, Cartier divisors $E_1, \dots, E_s$ on $X$ and an snc atlas $\mathcal{A}$ of $(E_i)$ of dimension $d$, indexed by $\{1, \dots, m\}$, such that $\mathcal{A}$ has the decomposition property and $\mathcal{O}_X(E_i) \cong \pi^* L_i$ in $\operatorname{Pic} X$ for each $i$.

Lean: `GlobalTheory.LogAtlas.exists_atlas_decomp`.

*Proof.* For each $x \in X$, choose an snc chart $C_x$ of $Y$ at $\pi(x)$. The open sets $\pi^{-1}(C_x)$ cover $X$, and $X$ is quasi-compact, since it is proper over $\mathbb{F}_p$. So finitely many of them, $V_1, \dots, V_m$, cover $X$. Each $V_k$ is affine, as the base change of an affine open, and it contains the generic point of $X$, as a nonempty open set of an integral scheme. On $V_k$, the pullbacks of the étale coordinates $t_l$ of the chart are étale coordinates over $\mathbb{F}_p$, and their images $x_{k,l}$ in the function field are nonzero.

The pullbacks of the sections $\sigma_i$ define Cartier divisors $E_i$ on $X$ with $\mathcal{O}_X(E_i) \cong \pi^* L_i$, and on $V_k$, $E_i$ has the local equation $x_{k, e(i)}$ or $1$, as in the chart. Let $J_k$ be the set of coordinates $l$ of the form $e(i)$. Then the union $Z$ of the supports of the $E_i$ meets $V_k$ in the points where some $x_{k,j}$, $j \in J_k$, is not a unit. A lemma on étale coordinates then gives conditions 1 and 2 of an atlas on $V_k$: étale coordinates give a basis of the differentials at each point, and the log units along a union of coordinate hyperplanes are the monomials in those coordinates times units. Condition 3 holds by construction. So the $V_k$ form an snc atlas of dimension $d$.

The function field has characteristic $p$, since $X$ lies over $\mathbb{F}_p$. Next, the charts of $Y$ give a Frobenius lift of $Z$, $(V_k)$ and $(x_k)$. On a chart of $Y$ over $\mathbb{Z}/p^2$, the map $t_l \mapsto t_l^p$ on the polynomial ring extends to a lift of the Frobenius, since the coordinates are étale; this lift fixes the coordinates as in condition 3 of a Frobenius lift and respects the log units, since the divisors are given by coordinates. We do not give the details of this step. Since $d < p$, the last theorem gives the decomposition property. $\square$

**Remark 9.2.6 (Formalization).** The second name `GlobalTheory.T.frobenius_decomposition_of_lift` is proved by `first | exact @… | …`, as in Section 1. The three lemmas of the first proof are `GlobalTheory.T.roundedTwist_localEquation_chart`, `GlobalTheory.T.log_sections_differential_closed` and `GlobalTheory.T.cartier_operator_log_sections`; the local reasons we give for items 2 and 3 are ours, and we read only the statements. The Frobenius lift in the second proof is `GlobalTheory.DI.isLifted_of_sncCharts` in [LiftedStalkMapGermAppLE.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/LiftedStalkMapGermAppLE.lean#L29), and conditions 1 and 2 of the atlas come from `GlobalTheory.T.etale_coordinates_log_chart`; again we read their statements. Projectivity is used only through properness, to get a finite cover. The smoothness of $X$ over $\mathbb{F}_p$ in [FrobeniusDecompositionAtlasModP.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/FrobeniusDecompositionAtlasModP.lean#L100) also follows from the snc charts of $Y$ by base change, so that hypothesis is redundant.
