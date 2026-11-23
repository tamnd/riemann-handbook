---
title: Finiteness of the schemes of homomorphisms and of actions
decls:
  - GlobalTheory.EndLoc.HomFixFinite.exists_finite_unramified
  - GlobalTheory.T.exists_finite_unramified_representing_polarizedHoms
  - GlobalTheory.ActFin.exists_actRep_finite
  - GlobalTheory.T.exists_finite_scheme_adjoint_actions_abelian
  - GlobalTheory.EndLoc.actRep_finite_unramified
  - GlobalTheory.T.adjointActions_order_finite_unramified_scheme
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness of the schemes of homomorphisms and of actions

This section proves two finiteness results over a locally noetherian base. The first says that the representing scheme for homomorphisms with fixed pullback is [[finite|N9C4X7XKE4]] and [[formally unramified|1JQX6HD8E5]] over the base. The second says that right actions of an order with the Rosati condition have a finite, formally unramified representing scheme. The second result is result 3 of the section on the Siegel problem with kernel killed by $d$, where it gives the scheme of principal Siegel objects with an action of an order. We keep the notation of the two previous sections and of Definition 8.7.2 for actions: order data $(O, a \mapsto \bar{a}, e_1, \dots, e_r, W, d_0)$, right actions $a \mapsto [a]$ with $[ab] = [b][a]$, and the Rosati condition.

### Homomorphisms with fixed pullback

We use three results. Let $A$ and $B$ be abelian schemes over a scheme $S$ with line bundles $L$ on $A$ and $M$ on $B$.

1. (Properness.) Assume that $L$ and $M$ are rigidified. Let $\pi : H \to S$ be a representing scheme for homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback. If $\pi$ is [[quasi-compact|41009J4M5D]], [[separated|X30G4V7VAJ]] and [[locally of finite type|AHTE5DVX61]], then $\pi$ is [[proper|9537RKBZPP]].
2. (Formal unramifiedness.) Every representing scheme $\pi : H \to S$ for homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback is formally unramified.
3. (Proper and unramified maps are finite.) Let $f : X \to Y$ be a map of schemes with $Y$ locally noetherian. If $f$ is proper and formally unramified, then $f$ is finite.

Result 2 is a form of the rigidity of homomorphisms of abelian schemes (Mumford, Fogarty and Kirwan, *Geometric Invariant Theory*, 3rd ed., Chapter 6, §1). A map $T \to H$ is a homomorphism over $T$, so a lift of a map $T_0 \to H$ along a closed immersion $T_0 \to T$ with square-zero ideal is a homomorphism over $T$ with a given restriction to $T_0$, and rigidity makes it unique. In result 3, a proper, formally unramified map is locally of finite type and unramified, so its fibres are finite. A proper map with finite fibres that is locally of finite presentation is finite (A. Grothendieck, *Éléments de géométrie algébrique IV*, Corollaire 18.12.4). Over a locally noetherian base, locally of finite type implies locally of finite presentation.

**Theorem 8.10.1 (Finite representing scheme).** Let $S$ be a locally [[noetherian|0670T59HGE]] scheme. Let $A$ and $B$ be [[abelian schemes|JDDXZ89N33]] over $S$ with rigidified, relatively ample line bundles $L$ on $A$ and $M$ on $B$. Then homomorphisms from $(A, L)$ to $(B, M)$ with fixed pullback have a representing scheme $\pi : H \to S$ such that $\pi$ is finite and formally unramified.

Lean: `GlobalTheory.EndLoc.HomFixFinite.exists_finite_unramified` (also `GlobalTheory.T.exists_finite_unramified_representing_polarizedHoms`, a second name).

*Proof.* By the [Theorem 8.9.3](/entry/hom-fix-finite-type/) of the previous section there is a representing scheme $\pi : H \to S$ such that $\pi$ is quasi-compact, separated and locally of finite type. By result 1, $\pi$ is proper. By result 2, $\pi$ is formally unramified. Since $S$ is locally noetherian, result 3 shows that $\pi$ is finite. $\square$

### The scheme of actions

Let $S$ be a scheme, $A$ a group scheme over $S$ and $P$ a line bundle on $A \times_S A$. For a map $t : T \to S$ and a group pullback $\varphi' : A' \to A$ along $t$ (Definition 8.2.5), we write $\varphi'_2 = \varphi' \times \varphi' : A' \times_T A' \to A \times_S A$. Then $(\varphi'_2)^* P$ is a line bundle on $A' \times_T A'$, and we can ask for the Rosati condition for it.

**Definition 8.10.2 (Scheme of actions).** Fix a ring $O$ and an additive map $a \mapsto \bar{a}$ on $O$. A *scheme of actions* for $(A, P)$ consists of a map $\pi : H \to S$, a group pullback $\varphi : A_H \to A$ along $\pi$ and a right action $a \mapsto [a]$ of $O$ on $A_H$ with the Rosati condition for $(\varphi_2)^* P$, with the following property. Let $t : T \to S$, let $\varphi' : A' \to A$ be a group pullback along $t$, and let $a \mapsto [a]'$ be a right action of $O$ on $A'$ with the Rosati condition for $(\varphi'_2)^* P$. Then there is a unique $g : T \to H$ with $\pi g = t$ for which there is a group pullback $\psi : A' \to A_H$ along $g$ with $\varphi \psi = \varphi'$ and $\psi [a]' = [a] \psi$ for every $a \in O$.

Lean: `GlobalTheory.EndLoc.ActRep`.

So $H$ is a fine moduli scheme over $S$ for right actions of $O$ on the base changes of $A$ that satisfy the Rosati condition. The map $\psi$ need not be unique; only $g$ is.

We now assume the following conditions on $P$:

- $P$ is trivial on $0 \times A$ and on $A \times 0$, that is, its pullbacks along $x \mapsto (0, x)$ and $x \mapsto (x, 0)$ have a generating section;
- $P$ is symmetric: $P \cong \sigma^* P$, where $\sigma(x, y) = (y, x)$;
- $\Delta^* P$ is relatively ample, where $\Delta(x) = (x, x)$.

These are the conditions that the line bundle of a Siegel object satisfies (Definition 8.1.5). For an order datum, let $A^r$ be the $r$-fold fibre power of $A$ with projections $p_1, \dots, p_r$, and put

$$\begin{aligned} L_d &= (\Delta^* P)^{\otimes d_0} \quad \text{on } A, \\ M_W &= \bigotimes_{u, v = 1}^{r} \big((p_u, p_v)^* P\big)^{\otimes W_{uv}} \quad \text{on } A^r. \end{aligned}$$

We use the following results. Let $A$ and $P$ satisfy the three conditions above, and fix an order datum.

4. (The two bundles.) $A^r$ is an abelian scheme, and $M_W$ is a rigidified, relatively ample line bundle on $A^r$. The line bundle $L_d$ is rigidified and relatively ample on $A$. The three conditions on $P$ are stable under pullback along $\varphi'_2$ for every group pullback $\varphi'$.
5. (Actions by relations.) There are integers $N_{jk}$ ($1 \le j \le m$), $c_k$ and $c_{ijk}$ with the following property. For every commutative group scheme $A'$ over any scheme and all endomorphisms $f_1, \dots, f_r$ of $A'$, there is a right action of $O$ on $A'$ with $[e_k] = f_k$ for all $k$ if and only if
$$\begin{aligned} &\textstyle\sum_k N_{jk} f_k = 0 \text{ for all } j, \qquad \sum_k c_k f_k = 1, \\ &\textstyle f_j f_i = \sum_k c_{ijk} f_k \text{ for all } i, j. \end{aligned}$$
6. (Equality is closed.) Let $S$ be locally noetherian and $u, v : A \to B$ maps of abelian schemes. There is a [[closed immersion|WWRWYSJDET]] $Z \to S$ such that for every $t : T \to S$ and every group pullback $\varphi' : A' \to A$ along $t$, we have $u \varphi' = v \varphi'$ if and only if $t$ factors through $Z$.
7. (The adjointness of two endomorphisms is closed.) Let $S$ be locally noetherian, let $A$ and $P$ satisfy the three conditions, and let $f, f'$ be endomorphisms of $A$. There is a closed immersion $Z \to S$ with this property. For every $t : T \to S$, every group pullback $\varphi' : A' \to A$ along $t$ and all endomorphisms $g, g'$ of $A'$ with $\varphi' g = f \varphi'$ and $\varphi' g' = f' \varphi'$, the line bundles $(g \times 1)^* (\varphi'_2)^* P$ and $(1 \times g')^* (\varphi'_2)^* P$ are isomorphic if and only if $t$ factors through $Z$.
8. (Rosati on generators.) Let $a \mapsto [a]$ be a right action of $O$ on $A$. If $([e_i] \times 1)^* P \cong (1 \times [\bar{e}_i])^* P$ for every $i$, then the action has the Rosati condition for $P$.
9. (Actions give test data.) Let $\varphi' : A' \to A$ be a group pullback along $t : T \to S$, with a right action with the Rosati condition for $(\varphi'_2)^* P$. Let $\Phi' = ([e_1]', \dots, [e_r]') : A' \to A'^r$. Then $\Phi'^* (M_W)' \cong L_d'$, where the primes denote pullbacks to $A'$ and $A'^r$.

In result 5 the integers come from a presentation of $O$: the $N_{j \cdot}$ span the relations among $e_1, \dots, e_r$, while $1 = \sum_k c_k e_k$ and $e_i e_j = \sum_k c_{ijk} e_k$. The order of $f_j f_i$ comes from $[e_i e_j] = [e_j][e_i]$. Result 8 holds because $a \mapsto \bar{a}$ is additive, $[\sum_k n_k e_k] = \sum_k n_k [e_k]$, and the Rosati condition is additive in $a$. The idea of result 9 is the following computation, where $P$ is additive in each variable. The Rosati condition and $[e_v \bar{e}_u] = [\bar{e}_u][e_v]$ give
$$\begin{aligned} ([e_u]' \times [e_v]')^* P' &\cong (1 \times [\bar{e}_u]'[e_v]')^* P' = (1 \times [e_v \bar{e}_u]')^* P', \end{aligned}$$
and the relation $\sum_{u, v} W_{uv} e_v \bar{e}_u = d_0$ of the order datum turns the weighted product over $u$ and $v$, pulled back along the diagonal, into $(\Delta^* P')^{\otimes d_0}$.

**Theorem 8.10.3 (The scheme of actions is finite).** Let $S$ be a locally noetherian scheme and $A$ an abelian scheme over $S$. Let $P$ be a line bundle on $A \times_S A$ that is trivial on $0 \times A$ and on $A \times 0$, symmetric, and with $\Delta^* P$ relatively ample. Fix an order datum $(O, a \mapsto \bar{a}, e_1, \dots, e_r, W, d_0)$. Then $(A, P)$ has a scheme of actions $\pi : H \to S$ with $\pi$ finite.

Lean: `GlobalTheory.ActFin.exists_actRep_finite` (also `GlobalTheory.T.exists_finite_scheme_adjoint_actions_abelian`, a second name).

*Proof.* By result 4 and the previous theorem, homomorphisms from $(A, L_d)$ to $(A^r, M_W)$ with fixed pullback have a finite representing scheme $\pi_0 : H_0 \to S$, with universal test datum $(A_0, B_0, \varphi_A, \varphi_B, \Phi)$. Then $H_0$ is locally noetherian. The group pullback $B_0$ of $A^r$ has projections $q_k : B_0 \to A_0$ over $p_k$, and we put $f_k = q_k \Phi$, an endomorphism of $A_0$. Choose integers $b_{ik}$ with $\bar{e}_i = \sum_k b_{ik} e_k$.

Let $Z \subseteq H_0$ be the intersection of the following closed subschemes. Result 6 gives the loci where $\sum_k N_{jk} f_k = 0$ for each $j$, where $\sum_k c_k f_k = 1$, and where $f_j f_i = \sum_k c_{ijk} f_k$ for each $i$ and $j$. Result 7, applied to $(\varphi_{A,2})^* P$ on $A_0$, gives for each $i$ the locus where $(f_i \times 1)^* P_0 \cong (1 \times \sum_k b_{ik} f_k)^* P_0$, with $P_0 = (\varphi_{A,2})^* P$. A finite intersection of closed subschemes is a closed subscheme, so $i_Z : Z \to H_0$ is a closed immersion. Let $\pi = \pi_0 i_Z$. A closed immersion is finite, so $\pi$ is finite.

Here is the key fact. Let $g : T \to H_0$, let $\psi : A' \to A_0$ be a group pullback along $g$, and let $g_1, \dots, g_r$ be endomorphisms of $A'$ with $\psi g_k = f_k \psi$. Then $g$ factors through $Z$ if and only if the $g_k$ satisfy the relations of result 5 and $(g_i \times 1)^* \psi_2^* P_0 \cong (1 \times \sum_k b_{ik} g_k)^* \psi_2^* P_0$ for each $i$. This follows from results 6 and 7, since $\psi$ is a group pullback and so $\psi u = \psi v$ implies $u = v$ for maps $u, v$ over $T$.

Let $A_H$ be the pullback of $A_0$ to $Z$, with $\varphi : A_H \to A$ the composite group pullback, and let $g_k$ be the pullbacks of $f_k$. By the key fact with $g = i_Z$, the $g_k$ satisfy the relations, so by result 5 there is a right action on $A_H$ with $[e_k] = g_k$. The key fact also gives the Rosati condition on each $e_i$, since $[\bar{e}_i] = \sum_k b_{ik} g_k$. By result 8, the action has the Rosati condition for $(\varphi_2)^* P$.

We prove the universal property. Let $t : T \to S$, let $\varphi' : A' \to A$ be a group pullback along $t$, and let $a \mapsto [a]'$ be a right action with the Rosati condition for $(\varphi'_2)^* P$. Let $B'$ be the pullback of $A^r$ along $t$ and $\Phi' = ([e_1]', \dots, [e_r]') : A' \to B'$, a map of group schemes. By result 9, $(A', B', \varphi', \varphi_{B'}, \Phi')$ is a test datum. So there is a unique $h_0 : T \to H_0$ with $\pi_0 h_0 = t$ that carries a map of test data, with group pullbacks $\psi_A : A' \to A_0$ and $\psi_B : B' \to B_0$ along $h_0$. Then $\psi_A [e_k]' = f_k \psi_A$, the $[e_k]'$ satisfy the relations of result 5, and the Rosati condition gives the line bundle condition, since $[\bar{e}_i]' = \sum_k b_{ik} [e_k]'$. By the key fact, $h_0 = i_Z z_0$ for some $z_0 : T \to Z$. The map $\psi_A$ lifts to a group pullback $\psi : A' \to A_H$ along $z_0$, and $\psi$ commutes with the actions on the generators $e_k$, so on all of $O$, since the $e_k$ span $O$. For uniqueness, let $z : T \to Z$ have the property. Then $i_Z z$ carries a map of test data for the datum of $\Phi'$, so $i_Z z = h_0 = i_Z z_0$. A closed immersion is a monomorphism, so $z = z_0$. $\square$

We also use the following result. For every scheme $S$, every abelian scheme $A$ over $S$, every line bundle $P$ on $A \times_S A$ and every additive map $a \mapsto \bar{a}$ on a ring $O$, every scheme of actions $\pi : H \to S$ for $(A, P)$ is formally unramified.

**Corollary 8.10.4 (Finite and unramified scheme of actions).** Under the hypotheses of the previous theorem, $(A, P)$ has a scheme of actions $\pi : H \to S$ with $\pi$ finite and formally unramified.

Lean: `GlobalTheory.EndLoc.actRep_finite_unramified` (also `GlobalTheory.T.adjointActions_order_finite_unramified_scheme`, a second name).

*Proof.* The previous theorem gives a scheme of actions with $\pi$ finite. By the result above, every scheme of actions is formally unramified. $\square$

**Remark 8.10.5 (Formalization).** Result 1 asks only that $L$ and $M$ are rigidified, not ample, and result 2 asks nothing of $L$ and $M$: [IsProperOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProperOfFiniteType.lean#L32) and [FormallyUnramifiedHomWithFixedPullbackSchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormallyUnramifiedHomWithFixedPullbackSchemeStatement.lean#L11). Result 3 asks only that the target is locally noetherian: [IsFiniteOfIsProperOfFormallyUnramified.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsFiniteOfIsProperOfFormallyUnramified.lean#L15). The proof of the theorem on actions obtains a finite and formally unramified representing scheme and discards the second property: [ExistsFiniteSchemeAdjointActionsAbelian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteSchemeAdjointActionsAbelian.lean#L88). The pullback of the three conditions in result 4 is a local alias of a lemma whose name speaks of a symmetric biextension, but the three conditions do not include a biextension structure: [ExistsFiniteSchemeAdjointActionsAbelian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteSchemeAdjointActionsAbelian.lean#L36) and [IsMonHomProdPow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsMonHomProdPow.lean#L20). In the scheme of actions, the classifying map is unique but the group pullback $\psi$ is only asked to exist: [ToRingActOpOfRingAct.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRingActOpOfRingAct.lean#L37). The groups of homomorphisms are written multiplicatively, so the sums in result 5 appear as products of integer powers. We read the statements of results 1 to 9 and of the formal unramifiedness of schemes of actions, not their proofs. The reasons given for results 2, 3, 5, 8 and 9 are ours.
