---
title: Fourier term systems with traits
decls:
  - GlobalTheory.T.uniformisedMembers_classSums_deeper_levels
  - GlobalTheory.Poinc.Sep.DeepSums.classSums_deeper
  - GlobalTheory.T.exists_fourierTermSystem_traits_chart_thetaModel
  - GlobalTheory.Poinc.Sep.exists_vPre_traits_chart
  - GlobalTheory.T.exists_fourierTermSystem_regular_traits_given_chart
  - GlobalTheory.Poinc.Sep.exists_chartMember_traitsR
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fourier term systems with traits

A Fourier term system collects, at one point of a rational model of a theta setup, the Fourier expansions of theta functions along many uniformized members at once. This section proves that every chart of the theta compactification is a member of a Fourier term system at some prime power level, and that the system also contains a member for each trait through the point. The proof assembles the [uniformized members](/entry/exists-u-mem/) of the previous section and proves the class sum condition at deeper levels. The result is the input of [separation at the centre](/entry/sep-st/).

We keep the notation of the previous sections. $(Z, z, i)$ is a theta compactification of a Siegel family $F$ of genus $g \ge 1$ and odd level $n \ge 3$, with an $E_8$ matrix $W$ and the theta integrality condition. For a theta setup $X_1$ and a point $z_1$ of its rational model $Z_1$ we write $\mathcal{O} = \mathcal{O}_{Z_1, z_1}$. For a lattice $X$, $\mu \in X^8$, $t_1, \dots, t_m$ and forms $\delta_k$, we write $\operatorname{mono}(t, \delta, \mu) = \prod_k t_k^{q_W(\delta_k)(\mu)}$ as before.

**Definition 9.12.1 (Fourier term pre-system).** A *Fourier term pre-system* $\Phi$ of rank at most $g$ over $\mathcal{O}$ consists of an index type $\Phi_Y$ and, for each $y \in \Phi_Y$:

1. a local CN domain $V_y$ and a local map $\mathrm{ev}_y : \mathcal{O} \to V_y$;
2. a free lattice $X_y$ of rank at most $g$;
3. elements $t_{y,1}, \dots, t_{y,m_y}$ of the maximal ideal of $V_y$, all nonzero, and symmetric forms $\delta_{y,k}$ on $X_y$ with $\delta_{y,k}(x, x) \ge 0$ and, for $x \ne 0$, some $k$ with $\delta_{y,k}(x, x) > 0$;
4. a label type $\Phi_Q$ and coefficients $u_y(\mu, c) \in V_y$ for $\mu \in X_y^8$ and $c \in \Phi_Q$, such that for each $\mu$ some $u_y(\mu, c)$ is a unit.

The *terms* are $T_y(\mu, c) = u_y(\mu, c)\operatorname{mono}(t_y, \delta_y, \mu)$. A *Fourier term system* of level $N_1$ is a pre-system with two more conditions. The first is an abelian bound: there is $C$ such that for each $y$ with $m_y = 1$ and each $x \ne 0$ some $h$ in the maximal ideal of $\mathcal{O}$ has $\mathrm{ev}_y(h)$ dividing $t_y^{C\delta_y(x, x)}$. The second is the Fourier condition `Four` of level $N_1$, on orbit sums of terms over a $p$-adic field at deeper levels, which we do not unfold.

Lean: `GlobalTheory.Poinc.VPre` (also `GlobalTheory.Poinc.VSys`, `GlobalTheory.Poinc.VPre.rescale`, `GlobalTheory.Poinc.VPre.toVSys`).

**Definition 9.12.2 (Class sums).** Let $\Phi$ be a pre-system, $y \in \Phi_Y$, $N \ge 1$, $\kappa \in X_y^8$, $c \in \Phi_Q$, and $\iota : V_y \to V'$ a map to a local ring. An element $x \in V'$ is a *class sum* for $(y, N, \kappa, c)$ if for each $j$ there is a finite set $S$ of $\mu \equiv \kappa \pmod N$ such that every other $\mu \equiv \kappa$ has $\sum_k q_W(\delta_{y,k})(\mu) \ge j$ and
$$x - \iota\Big(\sum_{\mu \in S} T_y(\mu, c)\Big) \in \mathfrak{m}_{V'}^{\,j}.$$
$\Phi$ is *exact* at level $N_1$ if each class sum for $(y, N_1, \kappa, c)$ with $\iota = \mathrm{id}$ is a value $\mathrm{ev}_y(h)$ with $h \in \mathcal{O}$. $\Phi$ has *class sums* at level $N_1$ if for each $y_0$ and $N_0$ there are:

1. a level $N \ge \max(N_0, 1)$ with $N_1 \mid N$, and maps $k_y : X_{y_0} \to X_y$, unimodular modulo $N$, with $k_{y_0} = \mathrm{id}$;
2. a finite Galois extension $L$ of the fraction field of $\mathcal{O}$, a maximal ideal $\mathfrak{z}$ of the integral closure $\mathcal{O}_L$, and functions $f(\kappa, c) \in \mathcal{O}_L$ that depend on $\kappa$ only modulo $N$;
3. for each $y$, a finite local pure map $\iota : V_y \to V'$ and $\mathrm{ev}' : \mathcal{O}_L \to V'$ over $\mathrm{ev}_y$ with $\mathfrak{z}$ as the inverse image of $\mathfrak{m}_{V'}$, such that $\mathrm{ev}'(f(\kappa, c))$ is a class sum for $(y, N, k_y\kappa, c)$;
4. for each $\sigma$ in the Galois group that fixes $\mathfrak{z}$, a map $\gamma$ of $X_{y_0}$ with $\det \gamma \equiv 1 \pmod N$ and $\gamma \equiv \mathrm{id} \pmod{N_1}$ such that $\sigma f(\kappa, c) = f(\gamma\kappa, c)$.

Lean: `GlobalTheory.Poinc.VPre.ClassSums` (also `GlobalTheory.Poinc.VPre.IsClassSum`, `GlobalTheory.Poinc.VPre.Exact`).

**Definition 9.12.3 (Traits and chart members).** Let $\Phi$ be a pre-system over $\mathcal{O}$. $\Phi$ *has traits* if for each trait $T$ of $F$, with ring $T_V$, uniformizer $\varpi$ and form $\beta$, and each local map $\mathrm{ev} : \mathcal{O} \to T_V$ that is regular at $z_1$ and lies over the point of $T$ in $Z$, there are $y$ with $m_y = 1$ and $V_y$ a principal ideal domain, an injective local $f : T_V \to V_y$ with $f \circ \mathrm{ev} = \mathrm{ev}_y$, and $X_y \cong X_T$ under which $t_y = f(\varpi)$ and $\delta_y = \beta$.

Let $Q$ be Mumford data over $V$ with periods $t^\delta$ and $\xi : \operatorname{Spec} V \to Z$. Then $y \in \Phi_Y$ is a *chart member* for $(Q, \xi)$ at level $N_1$, with $\rho : V \to V_y$, $e : X_y \cong X_Q$ and a bijection $h$ of indices, if $\rho$ is injective and finite, $\mathrm{ev}_y$ lies over $\xi$ along $\rho$, $t_{y,k} = \rho(t_{h(k)})$ and $\delta_{y,k} = \delta_{h(k)}$ under $e$, and there are $D$ and $e_8$ such that $(D, e_8)$ is a sharp refinement of $Q$ along $\rho$ and the terms are *theta terms* of $D$ at level $N_1$. The theta terms condition says that there are a theta family, torsion points $g_c$ of order dividing $N_1$ that cover all $N_1$-torsion over algebraically closed fields, and normalized frames, such that each $T_y(\mu, c)$ is the coefficient of the family at $e_8\mu$ for $g_c$, and some $T_y(0, c) = 1$. For a pre-system the last clause is dropped.

Lean: `GlobalTheory.Poinc.Sep.HasTraitsR` (also `GlobalTheory.Poinc.Sep.IsChartMember`, `GlobalTheory.Poinc.Sep.IsChartMemberP`, `GlobalTheory.Poinc.Sep.IsThetaTerms`).

Finally, $(\Phi, \mathrm{lab})$ is *geometric* for an action and a label $x_0$ if the theta function of $x_0$ divides at $z_1$, the labels $\mathrm{lab} : \Phi_Q \to \Gamma$ fill the set of dividing labels at $z_1$, and every $y$ has a uniformized member whose theta coefficients are the terms $T_y$ (Lean: `GlobalTheory.Poinc.Sep.IsGeo`).

**Theorem 9.12.4 (Class sums at deeper levels).** Let $X_1$ be a theta setup with an action, $z_1 \in Z_1$ with $\mathcal{O}$ a domain, $x_0$ a label, and $\Phi$ a pre-system over $\mathcal{O}$ with labels $\mathrm{lab}$. If $(\Phi, \mathrm{lab})$ is geometric, then $\Phi$ has class sums at level $rN$, where $r$ and $N$ are the ratio and level of the theta system of $X_1$.

Lean: `GlobalTheory.Poinc.Sep.DeepSums.classSums_deeper` (also `GlobalTheory.T.uniformisedMembers_classSums_deeper_levels`, a wrapper).

*Proof.* Fix $y_0$ and $N_0$, and choose a member $\mathfrak{m}_y$ for each $y$. A lemma on towers gives a deeper theta setup $X_2$ whose ratio of levels is at least $N_0$. A lemma on Galois extensions gives a finite Galois extension $L$ of the fraction field of $\mathcal{O}$ inside the base field of $X_2$, and a lemma on deeper points gives a point of the integral closure over $z_1$, with maximal ideal $\mathfrak{z}$. The dividing labels and their shifts persist on the deeper model. A lemma on class sum functions gives the functions $f$, rescaled by a power of a root of unity that comes from the base change of the members. For each $y$, a lemma on centred extensions gives a finite local pure $\iota : V_y \to V'$ and $\mathrm{ev}'$. The dividing theta constants generate the torsion labels integrally. A lemma on two members at the same point gives the maps $k_y$, and with the diagonal action on the eighth power this shows that $\mathrm{ev}'(f(\kappa, c))$ is a class sum. For $\sigma$ in the decomposition group of $\mathfrak{z}$, the same lemma on two members, applied to $\sigma$ and the deeper member, gives $\gamma$ with the stated congruences. $\square$

**Theorem 9.12.5 (Pre-systems with traits at a chart).** Let $Q$ be Mumford data over a local domain $V$ with monomial periods $t^\delta$, rank at most $g$, $t_k$ nonzero in the maximal ideal, and $\delta_k$ symmetric, nonnegative and jointly definite. Let $\xi : \operatorname{Spec} V \to Z$ with $Q$ uniformized over $\xi$, let $l$ be a prime dividing $n$ and $j_0 \in \mathbb{N}$. Then there are $j \ge j_0$, a theta setup $X_1$, a point $z_1$ with $\mathcal{O}$ a domain, a pre-system $\Phi$ over $\mathcal{O}$, an index $y$, data $\rho, e, h$ and a label $c_0$ such that:

1. $\Phi$ has traits, and $y$ is a chart member for $(Q, \xi)$ at level $(l^j)^2$;
2. each $u_{y'}(0, c_0)$ is a unit;
3. $m_{y'} \ne 1$ implies $y' = y$;
4. $\Phi$ is exact and has class sums at level $(l^j)^2$.

Lean: `GlobalTheory.Poinc.Sep.exists_vPre_traits_chart` (also `GlobalTheory.T.exists_fourierTermSystem_traits_chart_thetaModel`, a wrapper).

*Proof.* A lemma on prime power levels gives $j \ge j_0$, a theta setup $X_1$ of level $(l^j)^2$, a point $z_1$, a local CN domain $V_1$ with $\rho : V \to V_1$ injective and finite, an evaluation $\mathrm{ev}$ regular at $z_1$, and $D_0$ refining $Q$. The stalk $\mathcal{O}$ is a domain, a lemma gives an action on the eighth power, and $z_1$ has a dividing label $x_0$. As $Q$ is uniformized over $\xi$, $D_0$ has a uniformization $U_0$. The theorem on uniformized members gives a member $\mathfrak{m}_0$ at $(z_1, \mathrm{ev})$ with a sharp refinement of $Q$. Index $\Phi$ by one point $y$ for the chart and one point for each trait $T$ with a local regular $\mathrm{ev}_T$ over $T$. At $y$ take $(V_1, X_Q, \rho \circ t, \delta)$, and at $T$ take $(T_V, X_T, \varpi, \beta)$. Each trait has monomial periods with a definite form, so it has a uniformized member. A lemma on integral unit shifts gives the coefficients $u$ and clause 2. The traits clause holds with $f = \mathrm{id}$, and $y$ is a chart member with $e$ and $h$ the identities. The theta terms come from a lemma on torsion frames. The pair $(\Phi, \mathrm{lab})$ is geometric, so a lemma on values of functions gives exactness, and the previous theorem gives the class sums. $\square$

**Theorem 9.12.6 (Fourier term systems with traits).** In the setting of the previous theorem, there are $j \ge j_0$, a theta setup $X_1$, a point $z_1$, a Fourier term system $\Phi$ of level $(l^j)^2$ over $\mathcal{O}$, an index $y$ and data $\rho, e, h$ such that $\Phi$ has traits and $y$ is a chart member for $(Q, \xi)$ at level $(l^j)^2$.

Lean: `GlobalTheory.Poinc.Sep.exists_chartMember_traitsR` (also `GlobalTheory.T.exists_fourierTermSystem_regular_traits_given_chart`, a wrapper).

*Proof.* Apply the previous theorem with $\max(j_0, 1)$ in place of $j_0$. Then $j \ge 1$ and $N_1 = (l^j)^2 \ge 4 \ge 3$. A lemma on exact class sums gives the abelian bound, and a lemma on Galois class sums gives the Fourier condition. Put $v_{y'} = u_{y'}(0, c_0)^{-1}$. Since $m_{y'} \ne 1$ only at $y$, a lemma on the coefficient of index zero gives, for each $e'$, an $a \in \mathcal{O}$ with $\mathrm{ev}_{y'}(a) - v_{y'}^{-1} \in \mathrm{ev}_{y'}(\mathfrak{m}_{\mathcal{O}}^{e'})$ for all $y'$. A lemma on rescaling by approximated units shows that the rescaled pre-system $v\Phi$ still satisfies the Fourier condition, and the abelian bound does not depend on the coefficients. So $v\Phi$ is a Fourier term system, with the same traits. Its terms with $\mu = 0$ and $c = c_0$ equal $1$, so a lemma on theta terms upgrades the theta terms of the pre-system to theta terms, and $y$ is a chart member. $\square$

**Remark 9.12.7 (Formalization).** In `exists_chartMember_traitsR` the integral closedness `hIC` of the stalk is obtained but not used ([ExistsFourierTermSystemRegularTraitsGivenChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemRegularTraitsGivenChart.lean#L25)). The index type of the pre-system is `Option Tr`, with `Tr : Type 1` a sigma type over traits ([ExistsFourierTermSystemTraitsChartThetaModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemTraitsChartThetaModel.lean#L58)). The maps $e$ and $h$ of the chart member are `AddEquiv.refl _` and `Equiv.refl _`, and the label $c_0$ is `⟨x₀, AddSubgroup.subset_closure hx₀⟩` ([ExistsFourierTermSystemTraitsChartThetaModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFourierTermSystemTraitsChartThetaModel.lean#L120)). In `classSums_deeper` the congruences for $O$-linearity modulo $N$ are proved with the witness `0`, as $O = \mathbb{Z}$ here ([UniformisedMembersClassSumsDeeperLevels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedMembersClassSumsDeeperLevels.lean#L185), and again at line 320). The predicate `HasTraitsR` asks that `ev` is regular at $z_1$, while `HasTraits` for systems does not ([IsChartMember.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsChartMember.lean#L50)). The lemmas cited in the proofs have no entries in this part; we use only their statements.
