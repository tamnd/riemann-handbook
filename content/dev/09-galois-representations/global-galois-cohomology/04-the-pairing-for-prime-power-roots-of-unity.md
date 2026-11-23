---
title: The pairing for prime power roots of unity
decls:
  - GroundTheory.ProfCoh.zmodToQZ_gsCompactInv_gsCupClass
  - GroundTheory.ProfCoh.gsCompactInv_gsCupClass
  - GroundTheory.ProfCoh.gsPairingInput
  - GroundTheory.ProfCoh.BaseDualityHypotheses.of_gs
  - GroundTheory.ProfCoh.bijective_gs_compactZmodDualityMap
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The pairing for prime power roots of unity

This section starts the proof of Poitou-Tate duality for the [[Galois cohomology|9MPCZ3EAJM]] of a number field with restricted ramification. We work with the module $\mu_n$ of $n$-th roots of unity, for $n = \ell^k$ a prime power, and with cohomology with compact support at a finite set $S$ of finite places. There is a trace map from $H^3_c(G_S, \mu_n)$ to $\mathbb{Z}/n$, built from the local invariants. We prove that the cup product pairing
$$H^1(G_S, \mathbb{Z}/n) \times H^2_c(G_S, \mu_n) \to H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$$
is nondegenerate. The proof computes the pairing through class field theory: the cup product with a character $\chi$ is $\chi$ evaluated on an idele class. Then a formal argument gives duality in all degrees when $\mu_n \subseteq K$. The next section removes this condition. The base case of duality in the next section depends on all of this, and through it the step [EveryCharacter from Row0b](/step/every-character-of-row/).

The general theory is in [Galois cohomology of global fields](/learn/galois-cohomology/#global-fields), with [continuous cohomology](/learn/galois-cohomology/#continuous-cohomology) for the definitions.

### Setting

Throughout, $K$ is a finite extension of $\mathbb{Q}$ inside a fixed algebraic closure $\overline{\mathbb{Q}}$, and $S$ is a finite set of finite places of $K$. Let $K_S \subseteq \overline{\mathbb{Q}}$ be the maximal extension of $K$ that is unramified at all finite places outside $S$, and let $G_S = \operatorname{Gal}(K_S/K)$, a [[profinite group|KA0YDB6QXE]]. The real places of $K$ may ramify in $K_S$. For each $v \in S$ we fix an embedding $\iota_v$ of $\overline{\mathbb{Q}}$ into an algebraic closure of $K_v$ over $K$. It gives a continuous map $G_v = \operatorname{Gal}(\bar K_v/K_v) \to G_S$.

For $n \geq 1$ such that every prime of $K$ above a prime factor of $n$ lies in $S$, the group $\mu_n$ lies in $K_S$. We regard $\mu_n$ as a discrete $G_S$-module.

**Definition 2.4.1 (compact support cohomology).** Let $M$ be a discrete $G_S$-module. The *cohomology with compact support* $H^r_c(G_S, M)$ is the cohomology of the cone of the restriction map of continuous cochains
$$C^\bullet(G_S, M) \to \prod_{v \in S} C^\bullet(G_v, M).$$
It sits in the long exact sequence
$$\cdots \to \bigoplus_{v \in S} H^{r-1}(G_v, M) \to H^r_c(G_S, M) \to H^r(G_S, M) \to \bigoplus_{v \in S} H^r(G_v, M) \to \cdots.$$

Lean: `GroundTheory.ProfCoh.compactCohomologyRes`.

Only the finite places of $S$ enter the cone. The real places are treated in a later section, with the Tate modification.

**Definition 2.4.2 (the trace).** Let $n \geq 1$ with every prime above $n$ in $S$, and assume that $n$ is odd or that $K$ is totally complex. Assume $H^3(G_S, \mu_n) = 0$. Then the map $\bigoplus_{v \in S} H^2(G_v, \mu_n) \to H^3_c(G_S, \mu_n)$ is surjective. The *trace* $t : H^3_c(G_S, \mu_n) \to \mathbb{Z}/n$ is the unique homomorphism with
$$t\Big(\sum_{v} \xi_v\Big) = \sum_{v \in S} \operatorname{inv}_v(\xi_v),$$
where $\operatorname{inv}_v : H^2(G_v, \mu_n) \to \mathbb{Z}/n$ is the local invariant.

Lean: `GroundTheory.ProfCoh.gsCompactInv`.

The map is well defined because the sum of the local invariants vanishes on the image of $H^2(G_S, \mu_n)$. This is the reciprocity law for the Brauer group: a global class has local invariants with sum zero. The real places carry no invariant here. This is why $n$ must be odd or $K$ totally complex.

### The cup product and idele classes

The *$S$-idele class group* is $C_S = I_K/(K^\times \cdot U^S)$, where $U^S$ is the group of ideles with component $1$ at each $v \in S$ and a unit component at each finite $v \notin S$. The archimedean components of $U^S$ are free. Global [[class field theory|AA943HVK6Z]] gives an isomorphism
$$\Phi : \operatorname{Hom}_{\mathrm{cont}}(G_S, \mathbb{Z}/n) \xrightarrow{\ \sim\ } \operatorname{Hom}(C_S, \mathbb{Z}/n),$$
under the same condition that $n$ is odd or $K$ is totally complex.

Lean: `GroundTheory.ProfCoh.charEquiv`.

The group $H^2_c(G_S, \mu_n)$ is reached through the $S$-units $E_S$ of $K_S$ by the Kummer sequence $1 \to \mu_n \to E_S \to E_S \to 1$. A class of $H^1_c(G_S, E_S)$ is given by a *datum* $d = (t, (a_v)_{v \in S})$. Here $t \in K_S^\times$ is an element with $\sigma(t)/t \in E_S$ for each $\sigma \in G_S$, and $a_v \in K_v^\times$. The divisor of $t$ outside $S$ is then invariant under $G_S$, so it is the pullback of a divisor of $K$ outside $S$. The *class* of $d$ is the class in $C_S$ of the idele with component $a_v$ at $v \in S$ and that divisor, with the sign reversed, at the places outside $S$.

Lean: `GroundTheory.ProfCoh.gsUnitsClass`.

For a datum $d$ and a $1$-cocycle $z$ of $G_S$ in $\mathbb{Z}/n$, the *cup class* $c(d, z) \in H^3_c(G_S, \mu_n)$ is the cup product of the Kummer image $\delta(d) \in H^2_c(G_S, \mu_n)$ with the class of $z$. A cocycle $z$ is a continuous homomorphism $\chi_z : G_S \to \mathbb{Z}/n$, since $G_S$ acts trivially on $\mathbb{Z}/n$.

**Theorem 2.4.3 (cup class as a character value, in $\mathbb{Q}/\mathbb{Z}$).** Let $n = \ell^k$ with $\ell$ prime, with every prime of $K$ above $\ell$ in $S$, with $n$ odd or $K$ totally complex, and with $H^3(G_S, \mu_n) = 0$. Let $d$ be a datum and $z$ a cocycle. Let $\chi : G_S \to \mathbb{Z}/n$ be a continuous homomorphism with $\chi = \chi_z$. Then, in $\mathbb{Q}/\mathbb{Z}$,
$$t\big(c(d, z)\big) = \Phi(\chi)\big(\text{class of } d\big),$$
where $\mathbb{Z}/n$ is embedded in $\mathbb{Q}/\mathbb{Z}$ by $1 \mapsto 1/n$.

Lean: `GroundTheory.ProfCoh.zmodToQZ_gsCompactInv_gsCupClass`.

*Proof.* Lift $c(d, z)$ to a family $\xi = (\xi_v)$ in $\bigoplus_{v \in S} H^2(G_v, \mu_n)$. By the definition of $t$, the image of $t(c(d,z))$ in $\mathbb{Q}/\mathbb{Z}$ is $\sum_v \operatorname{inv}_v(\xi_v)$, and this is the sum of the invariants of the images of $\xi_v$ in the Brauer groups $H^2(G_v, \bar K_v^\times)$. Now push the cup class into compact cohomology with coefficients in the units. There, $c(d, z)$ becomes the cup product of the class of $d$ in $H^1_c(G_S, E_S)$ with $z$. That cup product is the image of a global class plus the family of local cup products $\delta(a_v) \cup \chi_v$, where $\chi_v$ is the restriction of $\chi$ to $G_v$. So the image of $\xi$ in the local Brauer groups differs from the family $(\delta(a_v) \cup \chi_v)_v$ by the localization of a global class, up to the image of local units at the places of $S$.

The global term has invariants with sum $0$, by the reciprocity law for the Brauer group of $K$, now with the contribution of $t$ outside $S$. By [[local class field theory|SHEN158T3M]], $\operatorname{inv}_v(\delta(a_v) \cup \chi_v) = \chi_v(\theta_v(a_v))$, where $\theta_v$ is the local reciprocity map. The sum of these values over $S$, together with the contribution of the divisor of $t$, is $\Phi(\chi)$ evaluated on the class of $d$, by the definition of $\Phi$ through the [reciprocity law](/learn/class-field-theory/#global-class-field-theory). $\square$

**Corollary 2.4.4 (cup class as a character value).** In the situation of the theorem,
$$t\big(c(d, z)\big) = \Phi(\chi_z)\big(\text{class of } d\big) \quad \text{in } \mathbb{Z}/n.$$

Lean: `GroundTheory.ProfCoh.gsCompactInv_gsCupClass`.

*Proof.* This is the theorem applied to $\chi = \chi_z$, together with the injectivity of $\mathbb{Z}/n \to \mathbb{Q}/\mathbb{Z}$. $\square$

### Nondegeneracy

**Theorem 2.4.5 (nondegeneracy of the pairing).** Let $\ell$ be a prime and $n = \ell^k$. Let $L$ be a finite extension of $\mathbb{Q}$ in $\overline{\mathbb{Q}}$ and $S'$ a finite set of finite places of $L$ that contains every place above $\ell$, with fixed embeddings at the places of $S'$. Assume that $\mu_n \subseteq L$, that $n$ is odd or $L$ is totally complex, and that $H^3(G_{S'}, \mu_n) = 0$. Then the pairing
$$H^1(G_{S'}, \mathbb{Z}/n) \times H^2_c(G_{S'}, \mu_n) \to \mathbb{Z}/n, \qquad (x, y) \mapsto t(y \cup x),$$
has zero left kernel and zero right kernel.

Lean: `GroundTheory.ProfCoh.gsPairingInput` (also `GroundTheory.ProfCoh.gsCompactInv_ker_left`, `GroundTheory.ProfCoh.gsCompactInv_ker_right`).

*Proof.* Write $K$ for $L$ and $S$ for $S'$. Two facts about $C_S$ are used. First, for each $b \in C_S$ there are an integer $m$ prime to $\ell$ and a datum $d$ with $m b$ equal to the class of $d$. Second, the class of $d$ is $0$ only if the class of $d$ in $H^1_c(G_S, E_S)$ is $0$.

Left kernel. Let $x \neq 0$ in $H^1(G_S, \mathbb{Z}/n)$, given by a nonzero character $\chi$. Then $\Phi(\chi) \neq 0$, so $\Phi(\chi)(b) \neq 0$ for some $b \in C_S$. Choose $m$ prime to $\ell$ and $d$ with $m b$ the class of $d$. By the corollary, $t(\delta(d) \cup x) = \Phi(\chi)(m b) = m\, \Phi(\chi)(b)$. This is not $0$, because $m$ is a unit in $\mathbb{Z}/\ell^k$. So $x$ is not in the left kernel.

Right kernel. Let $y$ be in the right kernel. If $k = 0$, then $n = 1$ and $y = 0$. Let $k \geq 1$. The Kummer map $H^1_c(G_S, E_S) \to H^2_c(G_S, \mu_n)$ is onto, and every class of $H^1_c(G_S, E_S)$ comes from a datum. So $y = \delta(d)$ for a datum $d$. Every homomorphism $f : C_S \to \mathbb{Z}/n$ has the form $\Phi(\chi)$, and $f(\text{class of } d) = t(y \cup x_\chi) = 0$. So the class of $d$ is divisible by $n$ in $C_S$: it equals $n b$. Choose $m$ prime to $\ell$ and $d'$ with $m b$ the class of $d'$. Then $m d - n d'$ has class $0$, so its class in $H^1_c(G_S, E_S)$ is $0$. Apply $\delta$: since $n$ kills the image of $n d'$, we get $m y = 0$. Also $\ell^k y = 0$. Since $m$ is prime to $\ell$, $y = 0$. $\square$

### Duality when $\mu_n \subseteq K$

The duality map in degrees $r + s = 3$ is
$$\Delta_{r} : H^r(G_S, \mathbb{Z}/n) \to \operatorname{Hom}\big(H^s_c(G_S, \mu_n), \mathbb{Z}/n\big), \qquad x \mapsto \big(y \mapsto t(y \cup x)\big).$$

**Definition 2.4.6 (base duality hypotheses).** Let $G$ be a profinite group with a finite nonempty family of maps $G_v \to G$, let $D$ be a discrete $G$-module killed by $n$, let $t_v : H^2(G_v, D) \to \mathbb{Z}/n$, and let $T : H^3_c(G, D) \to \mathbb{Z}/n$. The *base duality hypotheses* are:

1. $G$ acts trivially on $D$, and $D \cong \mathbb{Z}/n$;
2. the local pairing $H^1(G_v, \mathbb{Z}/n) \times H^1(G_v, D) \to \mathbb{Z}/n$ maps onto the dual, and the local pairing in degrees $2$ and $0$ is perfect;
3. $T$ is bijective, and $T$ of the image of $(\xi_v)$ is $\sum_v t_v(\xi_v)$;
4. $H^3(G, \mathbb{Z}/n) = 0$ and $H^3(G, D) = 0$;
5. $H^1(G, \mathbb{Z}/n)$ and $H^2_c(G, D)$ are finite;
6. the pairing of degrees $1$ and $2$ has zero left and right kernels;
7. the cup product is graded commutative under $T$ in degrees $1$ and $2$.

Lean: `GroundTheory.ProfCoh.BaseDualityHypotheses`.

Under these hypotheses the duality map is bijective for $r + s = 3$. In degree $r = 0$ this is the bijectivity of $T$. In degree $r = 3$ both sides vanish, because $H^0_c(G, D) = 0$ for a nonempty family. In degree $r = 1$ it follows from hypotheses 5 and 6 by counting. In degree $r = 2$ it follows from the long exact sequence, the local pairings and hypothesis 7.

**Theorem 2.4.7 (base duality hypotheses for $G_S$).** Let $S$ be nonempty, let $n = \ell^k$ with every prime above $\ell$ in $S$, and assume $\mu_n \subseteq K$. Assume that $n$ is odd or $K$ is totally complex, that $H^3(G_S, \mu_n) = 0$ and $H^3(G_S, \mathbb{Z}/n) = 0$, that $H^1(G_S, \mathbb{Z}/n)$ and $H^2_c(G_S, \mu_n)$ are finite, and that the pairing of degrees $1$ and $2$ has zero left and right kernels. Then $G_S$, the local groups $G_v$ for $v \in S$, the local invariants and the trace satisfy the base duality hypotheses for $D = \mu_n$.

Lean: `GroundTheory.ProfCoh.BaseDualityHypotheses.of_gs`.

*Proof.* Since $\mu_n \subseteq K$, the group $G_S$ fixes $\mu_n$, and a primitive root gives $\mu_n \cong \mathbb{Z}/n$. The local conditions are local Tate duality for $\mu_n$ over $K_v$, as in the [cohomology of local fields](/learn/galois-cohomology/#local-fields). The trace is bijective. It is onto because each local invariant is onto. It is injective because a family of local classes whose invariants have sum $0$ is the localization of a global class of $H^2(G_S, \mu_n)$, by the exact sequence of Brauer groups for the $S$-units, and such a family maps to $0$ in $H^3_c$. The formula for $T$ on local classes is the definition of the trace. The remaining hypotheses are assumptions of the theorem, except graded commutativity, which holds for the cup product of compact cohomology in degrees $1$ and $2$ because the map from local $H^2$ to $H^3_c$ is onto. $\square$

**Corollary 2.4.8 (duality when $\mu_n \subseteq K$).** In the situation of the theorem, the duality map
$$H^r(G_S, \mathbb{Z}/n) \to \operatorname{Hom}\big(H^s_c(G_S, \mu_n), \mathbb{Z}/n\big)$$
is bijective for all $r + s = 3$.

Lean: `GroundTheory.ProfCoh.bijective_gs_compactZmodDualityMap`.

*Proof.* This is the bijectivity of the duality map under the base duality hypotheses, applied to the hypotheses of the theorem. $\square$

**Remark 2.4.9 (Formalization).** The nondegeneracy statement quantifies over all number fields $L$ and sets $S'$; the hypothesis $\mu_n \subseteq L$ is part of the statement but the proof does not use it ([BaseMain.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseMain.lean#L56)). The corollary on cup classes takes the condition that $n$ is a unit outside $S$ as a separate hypothesis, although it follows from the other hypotheses ([BasePairing.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BasePairing.lean#L87)). The trace is defined by descent along a surjection ([BaseDefs.lean](lean:GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseDefs.lean#L307)). The comparison with $\mathbb{Q}/\mathbb{Z}$ is needed because local invariants of units take values in $\mathbb{Q}/\mathbb{Z}$.
