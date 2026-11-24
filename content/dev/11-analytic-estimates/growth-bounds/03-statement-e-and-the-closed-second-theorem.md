---
title: Statement E and the closed second theorem
decls:
  - Formalism.MainNotions.Pf14.theorem_II_of_cloud_bound_X
  - Formalism.MainNotions.Pf14.theorem_II_of_cloud_bound_Y
  - Formalism.MainNotions.Pf14.theorem_II_of_split_cloud_bounds
  - Formalism.MainNotions.TestSideCounting.theorem_II_closed_of_test_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Statement E and the closed second theorem

This section defines Statement E, a local lattice estimate at an unramified place, and proves the closed form of the second theorem: Statement E holds for every datum that satisfies the admissibility conditions and one remaining input, the test bound. The proof chains three reductions on the side of the target lattices, called cloud bounds, and uses [the plane Gram theorem](/entry/stmt/) of Section 2. The reductions of Section 5 remove the test bound, and the result is [Statement E](/entry/stmt-e/), which the local bound of Volume 15 uses ([the proof of the local bound](/entry/loc-proved/)).

### The local setting

**Definition 5.3.1 (Unramified quadratic setting).** Let $p$ be a prime and $n' \geq 1$. The setting consists of a discrete valuation ring $W$ with fraction field $\mathbb{Q}_q$, a discrete valuation ring $\mathcal{O}$ with fraction field $K$, an embedding $\iota : \mathbb{Q}_q \to K$, an automorphism $\sigma$ of $\mathbb{Q}_q$, a ring map $j : W \to \mathcal{O}$ and an element $w \in \mathcal{O}$. We assume that these data form a Hida setting at $p$ of degree $n'$, that $w$ is a uniformizer of $\mathcal{O}$, that $|\mathcal{O}/w\mathcal{O}| = p^{2n'}$, and that every integer is a square in $\mathcal{O}$.

A *lattice* in $\mathbb{Q}_q^{m+1}$ is the $W$-span of the columns of an invertible matrix. An *edge of rank $r$* is a pair of lattices $L'' \subseteq L$ with $pL \subseteq L''$ and $|L/L''| = p^{n'r}$. The *dual* of a lattice $L$ is the set of $x$ with $\sum_i x_iy_i \in W$ for all $y \in L$. See the Background on [lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices).

Fix $m \geq 1$ and a weight $\lambda_0 = (\lambda_{0,s})_{s < n'}$, with $\lambda_{0,s} \in \mathbb{Z}^{m+1}$. For even $s$ put $\lambda_s = \lambda_{0,s}$, and for odd $s$ let $\lambda_s$ be $-\lambda_{0,s}$ in reversed order. Let $V_\lambda$ be the tensor product over $s$ of the dual Weyl modules of [highest weight](/learn/representations/#highest-weights-and-branching) $\lambda_s$, realized as spaces of polynomials in the entries of an $(m+1) \times (m+1)$ matrix over $K$ (a factor is $0$ if $\lambda_s$ is not dominant). For a lattice $L$ let $H(L) \subseteq V_\lambda$ be the $\mathcal{O}$-lattice given by the tensor product of the integral structures at the twisted lattices $\iota\sigma^s(L)$. For an edge $e$ there is a second lattice $H_e(e)$, built in the same way from local data at the edge, and we put $R_e = w^{-A}H_e(e)$ with an integer $A = A(r, \lambda_0)$. Let $R'_e$ be the same scaling of the dual of $H_e(e)$.

**Definition 5.3.2 (Source and target modules).** Let $t \geq 0$. For a lattice $L''$ put
$$N_{\mathrm{src}}(t, L'') = w^{-t}H(L'') \cap \bigcap_{e:\ \mathrm{src}(e) = L''} R_e.$$
For a lattice $L$ put
$$N_{\mathrm{tgt}}(t, L) = w^{-t}H(L)^\vee \cap \bigcap_{e:\ \mathrm{tgt}(e) = L} R'_e.$$
The pairing of $F \in V_\lambda$ and $G \in V_\lambda^\vee$ is $b(F, G) = G(p^AF)$.

**Definition 5.3.3 (Good rank).** Let $A$ be an $\mathcal{O}$-module and let $\varphi_1, \dots, \varphi_M$ be maps from $A$ to $K$. We say that the family has *good rank $(n, D)$ at $\pi$* if there are an $\mathcal{O}$-linear map $u : \mathcal{O}^n \to A$ and a matrix $(M_{ji})$ over $\mathcal{O}$ with $\sum_i M_{ji}\varphi_i(u(x)) = \pi^Dx_j$ for all $x \in \mathcal{O}^n$ and all $j$.

So the functionals $\varphi_i$ detect a free submodule of rank $n$ of $A$, up to the factor $\pi^D$.

**Definition 5.3.4 (Local property LP').** Let $t, D, c^* \geq 0$ and $\kappa \in \mathbb{R}$. Property $\mathrm{LP}'(t, D, \kappa, c^*)$ holds if $4(D + 1) \leq c^*$ and, for every lattice $L$, there are edges $e_1, \dots, e_M$ of rank $r$ with target $L$ and vectors $F_i \in N_{\mathrm{src}}(t, \mathrm{src}(e_i))$ such that:

1. $F_i \in w^{c^*}R_{e'}$ for every other edge $e' \neq e_i$ of rank $r$ with the same source;
2. for some $n \geq (1 - \kappa)\dim V_\lambda$, the functionals $G \mapsto b(F_i, G)$ on $N_{\mathrm{tgt}}(t, L)$ have good rank $(n, D)$ at $p$.

Each $F_i$ lives on one edge and is $w^{c^*}$-small on the other edges from the same source. Together, the $F_i$ detect all but a fraction $\kappa$ of the target, up to $p^D$.

### Statement E

**Definition 5.3.5 (Statement E).** Let $C > 0$. *Statement E with constant $C$* says the following. Take the unramified quadratic setting, with $p \geq 13$ and $r \geq 2$. Take a set $T$ of indices $s < n'$, numbers $L_1$, $L_2$, $\delta$, $h$, $x$ for which the orbit hypothesis holds, a dominant weight $\lambda_0$ with base weights $a_s, b_s$ (with $a + c_{pp} \leq a_s \leq 2a - c_{pp}$ for $s \in T$), and numbers $Y \geq r$, $D_p$ and $c^*$. Let $N = N(r, \delta, h, x)$ be the window count and $G' = G'(r, \delta, h, x)$ the good exponent. Assume

$$\begin{aligned} &N^2 \leq r|T|, \quad C N^2\log a \leq m + 1, \quad N + 2r \leq m + 1 - r, \\ &256(m+1)^2|T|Y^2 \leq p^{L_1 - 1}, \quad C|T|(m+1)^2\log_p a \leq D_p, \\ &8(D_p + 1) \leq c^*, \end{aligned}$$

and a lower bound for $a$ of the form $C(m+1)^3r^2|T|\,p^{5G'}(c^* + r|T|c_0 + 2rn'c_{pp})\,Y \leq a$. Then for every integer $t$ at least a bound $t_0$, which is linear in $a$, the property
$$\mathrm{LP}'\Big(t, D_p, \frac{C|T|r^2(m+1)}{Y}, c^*\Big)$$
holds.

*Statement E for a datum $\mathcal{D}$* means: there is $C_0 > 0$ such that Statement E holds with every constant $C \geq C_0$.

The datum $\mathcal{D}$ of the proof does not enter Statement E. The statement is uniform over all unramified quadratic settings.

**Definition 5.3.6 (Admissibility of a datum).** A datum $\mathcal{D}$ with constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$ is *admissible* if it satisfies a list of $37$ conditions. The first two are combinatorial facts on good orbits: the structure of marked positions in an orbit, and the size of the good exponent $G'$, the window count $N$ and the set $T$ for $x$ large. The third is a dual height inclusion. The list also contains a valuation lemma, a filtered projection criterion, a few bad orbits condition, and the conditions from which the five properties of Section 1 follow.

Three more inputs enter. *Source cleaning with constants $(C_{La}', C_D, C_{sz})$* is a conjunction of six statements: a theta kernel expansion, a splitting package, a segment statement, an order lemma, a divisibility lemma and a class map estimate. *Plane Gram with constants $(C_H, C_E, C_6, C_{18})$* is the statement that the projection derivative estimate of Section 2 holds at every ring in the Hida setting that is admissible. A *step family* is a statement of the form: if $\mathcal{D}$ is admissible and source cleaning and plane Gram hold, then there are $C_{t0}, C_{D1}, C_1 > 0$ such that a step statement $S(C, C_{t0}, C_{D1}, C_{La})$ holds for all $C \geq C_1$. The *cloud bounds* and the *test bound* are the step families for four step statements: the cloud step, its forms X and Y, and the test step. The *primitive integrality* is the statement: if $\mathcal{D}$ is admissible, then there is $C_1 > 0$ such that a primitive step holds for all $C \geq C_1$.

The step statements concern the vectors that come from a basis of symbol spaces under a twisted substitution, the source vectors of LP', at the level $t_0 + |T|c_0 + \omega$ and with $D = C_{D1}|T|(m+1)^2\log_p a$. We do not unfold them.

### The reductions

**Proposition 5.3.7 (Cloud bounds).** Let $\mathcal{D}$ be admissible with constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$. Assume source cleaning with $(C_{La}', C_D, C_{sz})$ and plane Gram with $(C_H, C_E, C_6, C_{18})$.

1. If the cloud bound of form X holds with these constants, then Statement E holds for $\mathcal{D}$.
2. If the cloud bound of form Y holds with these constants, then Statement E holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.Pf14.theorem_II_of_cloud_bound_X` (also `Formalism.MainNotions.Pf14.theorem_II_of_cloud_bound_Y`, part 2).

*Proof.* There is a basic cloud form, and Statement E follows from it: from the cloud bound and the realisability of the sources (which holds for all constants), the degree five estimate of the second theorem gives Statement E. For part 1, the form X implies the basic form. The proof takes the few bad orbits condition from the admissibility list, keeps $C_{t0}$ and $C_{D1}$, and replaces $C_1$ by $\max(C_1, 2)$. For part 2, the form Y implies the form X with $C_1$ replaced by $\max(C_1, 1)$, and part 1 applies. $\square$

**Theorem 5.3.8 (Split cloud bounds).** Let $\mathcal{D}$ be admissible with constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$. Assume source cleaning with $(C_{La}', C_D, C_{sz})$, plane Gram with $(C_H, C_E, C_6, C_{18})$, the primitive integrality, and the test bound with all these constants. Then Statement E holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.Pf14.theorem_II_of_split_cloud_bounds`.

*Proof.* The primitive integrality and the test bound together give the cloud bound of form Y. This is part 2 of the [Proposition 5.3.7](/entry/theorem-ii-of-cloud-bound-y/) applied to it. $\square$

**Theorem 5.3.9 (Closed second theorem).** There is $C \geq 1$ with the following property. Let $\mathcal{D}$ be admissible with any constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$, and assume the test bound with source constants $(C, C + 1, C)$ and plane Gram constants $(26, 2, 24, 60)$. Then Statement E holds for $\mathcal{D}$.

Lean: `Formalism.MainNotions.TestSideCounting.theorem_II_closed_of_test_bound`.

*Proof.* A class map estimate gives a constant $C \geq 1$ such that source cleaning with $(C, C + 1, C)$ holds for every admissible datum: four of its six parts hold for every datum, the divisibility lemma follows from one admissibility condition, and the class map estimate follows from six of them. Admissibility gives the five properties of Section 1 at every admissible ring in the Hida setting, so [the plane Gram theorem](/entry/stmt/) with $C_H = 26$ gives plane Gram with $(26, 2, 24, 60)$. The primitive integrality holds for all constants. Now [the split cloud bounds theorem](/entry/theorem-ii-of-split-cloud-bounds/) gives Statement E. $\square$

So, once $C$ is fixed, the only open input is the test bound. Section 5 removes it.

**Remark 5.3.10 (Formalization).** Statement E is `tableLineDegreeFive.ConclusionE` with `aux₃` (TableLineDegreeFive.lean:30, 242), and `aux₃` ignores its argument `_D`. Its hypothesis $8(D_p + 1) \leq c^*$ is stronger than the condition $4(D + 1) \leq c^*$ inside LP' (UnramifiedQuadraticSetting.lean:216), so that part of LP' is free. The admissibility list is `tableLineDegreeFive.admitted` with $37$ conjuncts (TableLineDegreeFive.lean:234). The proof of part 1 of the Proposition reads the few bad orbits condition by a chain of $35$ projections `.2` and one `.1` (ScaleEdges/RestCloudOfX.lean:76). The Hida setting (`AdmissibleDVR`, `UniformizedDVR`), the orbit hypothesis (`IsGoodOrbit`), the dual Weyl modules, `Hten`, `LeAt`, and the step statements `CloudStep`, `CloudStepX`, `CloudStepY`, `TestStep` and `PrimStep` were not unfolded. The realisability of the sources is `sources_realisable_holds` and the primitive integrality is `rest6a`; neither was opened. The plane Gram input is assembled by `plane_gram_lemmas_of_admitted`, which builds the isotypic condition too, although the plane Gram theorem drops it (DualFockLinear/Closed.lean:23).
