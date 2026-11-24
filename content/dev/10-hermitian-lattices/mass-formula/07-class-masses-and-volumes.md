---
title: Class masses and volumes
decls:
  - PI.UnitaryGroupMassFormula.UJClassMass.unitary_class_mass
  - PI.UnitaryGroupMassFormula.UJClassMass.uJClassMass_of_herm
  - Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.genus_class_mass
  - Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.classMass_of_D7
  - Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.volume_mass_of_genus_rank
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Class masses and volumes

For a definite Hermitian space the adelic quotient $U_J(F) \backslash U_J(\mathbb{A}_{F,f})$ is a finite union of double cosets, by the [finiteness of classes](/entry/adelic-class-set-finite/) of the last section. This section proves the [class mass formula](/entry/unitary-class-mass-hermitian/): the sum over the classes of $1 / \#\operatorname{Stab}$ is the mass of the genus of the base lattice. Then it turns the class mass formula into a statement on volumes: the volume of a fundamental domain for $U_J(F)$ in $U_J(\mathbb{A}_{F,f})$ equals the mass. The volume form is the one that the [local matching of theta lifts](/step/theta-local-matching/) uses, since there the integrals over the adelic quotient are compared with local densities. We keep the notation of the earlier sections: $E/F$ is a CM extension with involution $a \mapsto \bar{a}$, the matrix $J$ is Hermitian, $h(x, y) = x^* J y$, and $L_0 \subseteq E^m$ is a lattice. For lattices and their genera see [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

### Genus, classes and mass

**Definition 7.7.1 (Genus and class).** Let $L_0 \subseteq E^m$ be an $\mathcal{O}_E$-lattice. The *genus* of $L_0$ is the set of lattices $N \subseteq E^m$ with $N_v = g_v L_{0,v}$ for some $g_v \in U_J(F_v)$ at every finite place $v$, and $N_v = L_{0,v}$ for almost all $v$. Two lattices $N, N'$ of the genus are in the same *class* if $N' = \gamma N$ for some $\gamma \in U_J(F)$.

The group $G_f = U_J(\mathbb{A}_{F,f})$ acts on the genus: for $g \in G_f$ let $g L_0$ be the lattice with completions $g_v L_{0,v}$. Let $K \subseteq G_f$ be the stabilizer of $L_0$. Then $g \mapsto g L_0$ is a bijection from $G_f / K$ onto the genus, and $U_J(F) \backslash G_f / K$ is the set of classes. For $g \in G_f$ let
$$\Gamma_g = U_J(F) \cap g K g^{-1},$$
the group of global isometries that fix the lattice $g L_0$.

**Definition 7.7.2 (Mass).** Assume that $h$ is definite at every infinite place. Then each $\Gamma_g$ is finite. Let $g_1, \dots, g_r$ be a set of representatives of $U_J(F) \backslash G_f / K$. The *mass* of the genus of $L_0$ is
$$\operatorname{mass}(h, L_0) = \sum_{i=1}^{r} \frac{1}{\#\Gamma_{g_i}}.$$

The sum does not depend on the choice of representatives, since $\Gamma_{\gamma g k} = \gamma \Gamma_g \gamma^{-1}$ for $\gamma \in U_J(F)$ and $k \in K$. The mass counts each class with weight $1 / \#\operatorname{Aut}$, as in the mass formula of Smith, Minkowski and Siegel for quadratic forms. This weight makes the mass additive under change of level and makes it a volume, as the last theorem of this section shows.

### Inputs

The class mass formula rests on four statements. The first two are about lattices; the last two are about the adelic group.

**Theorem 7.7.3 (Hermitian approximation).** Let $N$ be a lattice in the genus of $L_0$ and let $P$ be a finite set of maximal ideals of $\mathcal{O}_E$. Then there is $\gamma \in U_J(E)$ with $(\gamma L_0)_{\mathfrak{p}} = N_{\mathfrak{p}}$ for all $\mathfrak{p} \in P$.

This is a form of strong approximation for the lattices of a genus. We take it from six parts: a local switching lemma for lattices, a localization of tensor products, a lemma that two lattices of the same genus agree at almost all places, the choice of an auxiliary place, a bound on the coefficients, and a condition on Gram matrices. We do not repeat them.

**Theorem 7.7.4 (Lattice step).** Assume that $h$ has signature $(m, 0)$ at every infinite place. For each $g \in G_f$ the lattice $g L_0$ lies in the genus of $L_0$.

**Theorem 7.7.5 (Surjectivity step).** Under the same signature condition, each lattice $N$ in the genus of $L_0$ is $g L_0$ for some $g \in G_f$.

**Theorem 7.7.6 (Completion of a translated lattice).** Let $L \subseteq E^m$ be a set with $c\,\mathcal{O}_E^m \subseteq L$ and $c L \subseteq \mathcal{O}_E^m$ for some nonzero $c \in \mathcal{O}_F$. Let $\hat{L} \subseteq (\mathbb{A}_{F,f} \otimes_F E)^m$ be its completion. Then for $g \in G_f$ and $y \in (\mathbb{A}_{F,f} \otimes_F E)^m$ we have $g^{-1} y \in \hat{L}$ if and only if $y \in \widehat{gL}$.

**Lemma 7.7.7 (Coordinate bounds).** Each lattice $L_0 \subseteq E^m$ satisfies $c\,\mathcal{O}_E^m \subseteq L_0$ and $c L_0 \subseteq \mathcal{O}_E^m$ in the coordinates of a basis, for some nonzero $c \in \mathcal{O}_F$.

### The class mass formula

**Theorem 7.7.8 (Class mass formula).** Let $E/F$ be a CM extension, and let $J$ be an $m \times m$ Hermitian matrix over $E$ that is nondegenerate. Let $L_0 \subseteq E^m$ be a lattice. Assume that $h$ has signature $(m, 0)$ at every embedding $\tau : F \to \mathbb{R}$, and that each embedding of $E$ sends $\bar{a}$ to the complex conjugate of $a$. Let $g_1, \dots, g_r \in G_f$ be elements such that every $x \in G_f$ is $\gamma g_i k$ for some $i$, some $\gamma \in U_J(F)$ and some $k \in K$, and such that $\gamma g_i k = \gamma' g_j k'$ implies $i = j$. Then
$$\sum_{i=1}^{r} \frac{1}{\#\Gamma_{g_i}} = \operatorname{mass}(h, L_0).$$

Lean: `PI.UnitaryGroupMassFormula.UJClassMass.unitary_class_mass` (also `PI.UnitaryGroupMassFormula.UJClassMass.uJClassMass_of_herm`, the same conclusion from Hermitian approximation).

*Proof.* The first step is the surjectivity step. Let $N$ be a lattice of the genus. The lattices $N$ and $L_0$ agree at all places outside a finite set $P$. Hermitian approximation gives $\gamma \in U_J(E)$ with $(\gamma L_0)_{\mathfrak{p}} = N_{\mathfrak{p}}$ for $\mathfrak{p} \in P$. A local switching at one place then puts the components together into $g \in G_f$ with $g L_0 = N$. With the lattice step this shows that $g \mapsto g L_0$ is a bijection from $G_f / K$ onto the genus.

The second step is the lattice modification. The map $g \mapsto g L_0$ is equivariant for $U_J(F)$, so it induces a bijection from $U_J(F) \backslash G_f / K$ onto the set of classes of the genus. The stabilizer of $g L_0$ in $U_J(F)$ is $\Gamma_g$. So the given representatives $g_i$ give one lattice in each class, and each class once.

The third step identifies the sum with the mass. The coordinate bounds place $L_0$ between $c\,\mathcal{O}_E^m$ and $c^{-1}\mathcal{O}_E^m$, so the theorem on the completion of a translated lattice applies: the lattice $g L_0$ is read off from the adelic translate $g \hat{L}_0$, and its stabilizer in $U_J(F)$ is $\Gamma_g$. Since $h$ is definite, $U_J(F_\infty)$ is compact and $\Gamma_g$ is discrete in it, so each $\Gamma_{g_i}$ is finite. The sum of $1/\#\Gamma_{g_i}$ over the classes is the mass by the definition, and the bijection of the second step shows that it does not depend on the set of representatives. $\square$

For the use in the theta lifts the formula is restated for the data of a family. We write $\mathcal{D}$ for the data of the definite setting: the fields $F$ and $E$, the signature data and a fixed volume function $W \mapsto \operatorname{vol}(W)$ on Hermitian spaces $W$ over $E$, together with a number $\operatorname{mass}_{\mathcal{D}}(n)$ for each rank $n$.

**Corollary 7.7.9 (Class mass for the definite data).** For the data $\mathcal{D}$, the class mass holds: for each Hermitian space $W$ of the data with signature $(\operatorname{rk} W, 0)$ at all $\tau$ and for each full set of representatives $g_1, \dots, g_r$ of the double cosets of $W$, the sum of $1 / \#\Gamma_{g_i}$ is the mass of the genus of the standard lattice of $W$.

Lean: `Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.classMass_of_D7` (also `Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.genus_class_mass`, a second name of the class mass formula).

*Proof.* This is the class mass formula applied to the Hermitian space $W$ and its standard lattice, through the passage from the genus classes to the class mass. $\square$

### Volume equals mass

**Definition 7.7.10 (Volume tie).** The data $\mathcal{D}$ has the *volume tie* if for each Hermitian space $W$ that satisfies the signature condition, of signature $(P, Q)$ at all $\tau$, there is a Haar measure $\mu$ on $U_W(\mathbb{A}_{F,f})$ of the normalized kind, and for each such $\mu$ there is a fundamental domain $\mathcal{F}$ of $U_W(F)$ in $U_W(\mathbb{A}_{F,f})$, and for each such $\mu$ and $\mathcal{F}$,
$$\mu(\mathcal{F}) = \operatorname{vol}(W).$$

**Definition 7.7.11 (Genus mass at rank $n$).** The data $\mathcal{D}$ has the *genus mass at rank $n$* if $\operatorname{mass}(h_W, L_{0,W}) = \operatorname{mass}_{\mathcal{D}}(n)$ for each definite space $W$ of rank $n$ with the signature condition.

**Theorem 7.7.12 (Volume equals mass).** Let $\mathcal{D}$ be definite data with the volume tie, and let $n \geq 0$. Assume the genus mass at rank $n$. Then for each Hermitian space $W$ of the data with the signature condition, signature $(n, 0)$ at all $\tau$ and rank $n$,
$$\operatorname{vol}(W) = \operatorname{mass}_{\mathcal{D}}(n).$$

Lean: `Formalism.L2.GlobalTheoryTheory.GenusMassVolumes.volume_mass_of_genus_rank`.

*Proof.* Let $W$ be such a space. The volume tie gives a Haar measure $\mu$ and a fundamental domain $\mathcal{F}$ with $\mu(\mathcal{F}) = \operatorname{vol}(W)$. The normalization of $\mu$ gives $\mu(K) = 1$ for the stabilizer $K$ of the standard lattice. By the [finiteness of classes](/entry/adelic-class-set-finite/) at rank $n$ there are representatives $g_1, \dots, g_r$ of $U_W(F) \backslash G_f / K$. The double coset $U_W(F)\, g_i K$ meets $\mathcal{F}$ in a set of measure
$$\frac{\mu(g_i K)}{\#\Gamma_{g_i}} = \frac{\mu(K)}{\#\Gamma_{g_i}} = \frac{1}{\#\Gamma_{g_i}},$$
because $\Gamma_{g_i}$ is finite and acts on $g_i K$ with each orbit counted $\#\Gamma_{g_i}$ times. Summing over $i$ gives $\mu(\mathcal{F}) = \sum_i 1 / \#\Gamma_{g_i}$. The corollary on the class mass for the data turns this sum into the mass of the genus, and the genus mass at rank $n$ turns that into $\operatorname{mass}_{\mathcal{D}}(n)$. $\square$

The genus mass at rank $n$ follows from the genus mass for all ranks, and so the volume equals the mass for every rank once the volume tie holds.

**Remark 7.7.13 (Formalization).** The class mass formula keeps two theorems as hypotheses of its proof: the lattice modification and the completion of a translated lattice ([UJClassMassOfDeep.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/UJClassMassOfDeep.lean#L82)). Hermitian approximation is stated for $\gamma \in U_J(E)$ and maximal ideals of $\mathcal{O}_E$, without the signature condition ([PSurjS.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/PSurjS.lean#L9)). The variant of the class mass statement in UJClassMassAlt.lean also asks for an element $\theta$ with $\bar{\theta} \neq \theta$; the statement used here does not. The file that defines the class mass formula ends with `#check` and `#print axioms` commands ([UnitaryClassMass.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/UnitaryClassMass/UnitaryClassMass.lean#L22)). The second name of the class mass formula is a pure rename ([PacketStatementOfIndependence.lean](lean:Formalism/LocalToGlobal/GlobalTheory/GL5/PacketStatementOfIndependence.lean#L10)). We did not unfold the volume function, the number $\operatorname{mass}_{\mathcal{D}}(n)$, the normalized kind of Haar measure, or the proof of the completion statement; the measure computation in the last proof follows the steps of its proof (the volume tie, $\mu(K) = 1$, the class data), not a line by line reading.
