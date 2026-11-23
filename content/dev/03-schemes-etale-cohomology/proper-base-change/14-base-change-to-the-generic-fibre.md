---
title: Base change to the generic fibre
decls:
  - UpperTheory.Et.E3.n64
  - UpperTheory.Et.E3.n8
  - UpperTheory.Et.E3.main
  - UpperTheory.Et.etale_base_change_of_duality
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base change to the generic fibre

In this section we prove axiom E3. Let $T$ be an absolutely integrally closed local domain with fraction field $K$, and let $X$ be smooth over $T$. Then the generic fibre $X_K \to X$ is an equivalence for $\mathbb{Z}/q(i)$. This is a form of the local acyclicity of smooth maps. The proof adds one variable at a time to $T$. The step from $A$ to $A[x]$ uses the descent principle of section 13 twice, once in the proposition on strictly henselian pairs below and once in the step itself. With the theorem of section 12, this completes the proof of the axioms E1 to E4, which the earlier sections of the chapter and other chapters of the Galois row use.

### Residually algebraic maps

Throughout, $q \geq 1$ and $i$ are fixed, and we use the language of section 13: equivalences of rings, base change along a map, ind-étale maps and maps surjective on spectra. We assume the axioms A1 to A5, A9, B1, B2, B4, C3 and C4 of section 1. Other chapters of this volume prove them.

**Definition 3.14.1 (Residually algebraic map).** A ring map $k : A \to C$ is *residually algebraic* if for every prime $\mathfrak{Q}$ of $C$ and every $z \in C$ there is a polynomial $p \in A[X]$ such that some coefficient of $p$ does not map into $\mathfrak{Q}$ and $p(z) \in \mathfrak{Q}$.

So $k$ is residually algebraic if the image of each $z$ in $C/\mathfrak{Q}$ is a root of a nonzero polynomial with coefficients from $A$.

**Definition 3.14.2 (Étale base change over a map).** Let $k : T \to K$ and $t : T \to A$ be ring maps. We say that $k$ has *étale base change over $t$* if $k$ has base change along $c \circ t$ for every étale map $c : A \to B$.

### Facts that we take as given

We take as given the following facts.

1. *(Residually algebraic maps.)* Residually algebraic maps are closed under composition and under pushouts. If $g \circ f$ is residually algebraic, then so is $g$. Étale maps, integral maps and localizations are residually algebraic.
2. *(Passage to ind-étale maps.)* Let $\varphi : A \to Y$ be a ring map with $q$ a unit in $A$. If $\varphi$ has base change along every étale map, then it has base change along every ind-étale map. This rests on B1.
3. *(Strict henselizations.)* For every prime $\mathfrak{r}$ of a ring $A$ there is an ind-étale map $f : A \to O$ with $O$ strictly henselian and $\mathfrak{r} = f^{-1}(\mathfrak{m}_O)$. A composite of ind-étale maps is ind-étale.
4. *(Strictly henselian rings.)* Every ring map between strictly henselian rings in which $q$ is a unit is an equivalence. The proof uses B2 in positive degrees and compares sections in degree $0$.
5. *(Covers.)* Every ring $C$ has an integral injective map $C \to D_0$ with $D_0$ absolutely integrally closed. Every absolutely integrally closed ring $D_0$ has an integral map $D_0 \to D$, surjective on spectra, such that every local ring $D_{\mathfrak{r}}$ is an absolutely integrally closed domain. Localizations are ind-étale, and integral injective maps are surjective on spectra.
6. *(The local case.)* Let $A$ and $X$ be strictly henselian, $q$ a unit in $A$, and $h : A[x] \to X$ ind-étale such that $A \to X$ is a local homomorphism. Let $C$ be an absolutely integrally closed local domain and $c : A \to C$ residually algebraic. Then $A \to X$ has base change along $c$. The proof passes to an integral local subring of $C$, and uses fact 7, the fact that an absolutely integrally closed local domain is strictly henselian, and fact 4.
7. *(Polynomial base change.)* Let $T$ be an absolutely integrally closed local domain with fraction field $K$, and $q$ a unit in $T$. Then $T \to K$ has base change along $T \to T[x] \to X$ for every ind-étale map $T[x] \to X$. For étale maps this is axiom C3, and fact 2 extends it to ind-étale maps.
8. *(From polynomial rings to smooth schemes.)* Let $k : T \to K$ be a ring map such that $k$ has étale base change over $T \to T[x_1, \dots, x_n]$ for every $n$. Then for every smooth map $X \to \operatorname{Spec} T$, the projection $X \times_{\operatorname{Spec} T} \operatorname{Spec} K \to X$ is an equivalence for $\mathbb{Z}/q(i)$. Its proof works Zariski locally on $X$, treats affine $X$, and uses that a smooth scheme is locally étale over an affine space.

We also use the rules for equivalences: a composite of equivalences is an equivalence, and if $f$ and one of $g \circ f$ and $g$ are equivalences, then so is the third map. Base change along $c \circ t$ for $k$ is the same as base change along $c$ for the pushout of $k$ along $t$, since pushout squares paste.

### Strictly henselian pairs

**Proposition 3.14.3 (Base change for strictly henselian pairs).** Let $A$ and $X$ be strictly henselian, $q$ a unit in $A$, and $h : A[x] \to X$ ind-étale such that $\varphi : A \to A[x] \to X$ is a local homomorphism. Then $\varphi$ has base change along every residually algebraic map $c : A \to C$.

Lean: `UpperTheory.Et.E3.n64`.

*Proof.* We apply [the descent principle](/entry/n9/) to $\varphi$ and the class $P$ of residually algebraic maps $A \to C$. By fact 1, $P$ is closed under étale maps. It is closed under pushouts: let $c : A \to C$ be in $P$, and let $f : C \to D$ and $g : C \to E$ be such that $f \circ c$ and $g \circ c$ are in $P$, with pushout maps $u : D \to Z$ and $v : E \to Z$. Then $f$ is residually algebraic by right cancellation, $v$ is a pushout of $f$, and $u \circ f \circ c = v \circ g \circ c$ is a composite of maps in $P$.

Let $c : A \to C$ be in $P$. Fact 5 gives integral maps $g_0 : C \to D_0$ and $g_1 : D_0 \to D$, and we put $g = g_1 \circ g_0$. Then $g$ is integral and surjective on spectra, and $g \circ c$ is in $P$, since $g$ is integral. Let $\mathfrak{r}$ be a prime of $D$, and let $o : D \to D_{\mathfrak{r}}$ be the localization. It is ind-étale, and the maximal ideal of $D_{\mathfrak{r}}$ lies over $\mathfrak{r}$. The ring $D_{\mathfrak{r}}$ is an absolutely integrally closed local domain, and $o \circ g \circ c$ is residually algebraic by fact 1. By fact 6, $\varphi$ has base change along $o \circ g \circ c$. So $\varphi$ has base change at the points of $D$, and the descent principle gives the result. $\square$

### Adding a variable

**Proposition 3.14.4 (Adding a variable).** Let $k : T \to K$ be residually algebraic, let $q$ be a unit in $T$, and let $t : T \to A$ be a ring map such that $k$ has étale base change over $t$. Then $k$ has étale base change over $T \to A \to A[x]$.

Lean: `UpperTheory.Et.E3.n8`.

*Proof.* Let $\varphi : A[x] \to K \otimes_T A[x]$ be the pushout of $k$. Since pushout squares paste, it is enough to show that $\varphi$ has base change along every étale map $c : A[x] \to U$. We apply the descent principle to $\varphi$ with the class $P$ of étale maps out of $A[x]$ and the cover $g = \mathrm{id}$. Étale maps are closed under composition and pushouts, so $P$ is closed under étale maps and pushouts.

Let $c : A[x] \to U$ be étale and $\mathfrak{r}$ a prime of $U$. We first construct a strictly henselian model at $\mathfrak{r}$. Let $\mathfrak{r}_A$ be the preimage of $\mathfrak{r}$ in $A$. Fact 3 gives an ind-étale map $f : A \to A'$ with $A'$ strictly henselian and maximal ideal over $\mathfrak{r}_A$. The ring $U' = U \otimes_A A'$ is étale over $A'[x]$, and it has a prime $\mathfrak{r}'$ over $\mathfrak{r}$ and over $\mathfrak{m}_{A'}$. Fact 3 gives an ind-étale map $U' \to X$ with $X$ strictly henselian and maximal ideal over $\mathfrak{r}'$. Let $h : A'[x] \to U' \to X$ and $o : U \to U' \to X$. Both are ind-étale, the maximal ideal of $X$ lies over $\mathfrak{r}$, the map $A' \to X$ is local, and the two maps $A \to X$ through $A[x]$ and $U$, and through $A'$ and $A'[x]$, agree.

It remains to show that $\varphi$ has base change along $o \circ c$, that is, that $k$ has base change along $T \to X$. Let $\psi : A \to K \otimes_T A$ be the pushout of $k$ along $t$. By hypothesis $\psi$ has base change along every étale map, so by fact 2 it has base change along $f$. Thus $A' \to Y_1 = K \otimes_T A'$ is an equivalence. This map is a pushout of $k$, so it is residually algebraic by fact 1. By [the proposition on strictly henselian pairs](/entry/n64/), applied to $h$ and to $A' \to Y_1$, the map $Y_1 \to X \otimes_{A'} Y_1$ is an equivalence. By fact 4, $A' \to X$ is an equivalence. The composites $A' \to Y_1 \to X \otimes_{A'} Y_1$ and $A' \to X \to X \otimes_{A'} Y_1$ agree. The first is an equivalence, so the second is one, and since $A' \to X$ is an equivalence, so is $X \to X \otimes_{A'} Y_1 = K \otimes_T X$. This holds for every pushout, so $k$ has base change along $T \to X$.

So $\varphi$ has base change at the points of $U$, and the descent principle shows that $\varphi$ has base change along $c$. $\square$

### The theorem

**Theorem 3.14.5 (Base change to the generic fibre).** Let $T$ be an absolutely integrally closed local domain with fraction field $K$, let $q \geq 1$ be a unit in $T$, and let $p : X \to \operatorname{Spec} T$ be smooth. Then for every $i$ the projection $X \times_{\operatorname{Spec} T} \operatorname{Spec} K \to X$ is an equivalence for $\mathbb{Z}/q(i)$. This is axiom E3.

Lean: `UpperTheory.Et.etale_base_change_of_duality` (also `UpperTheory.Et.E3.main`, the same statement with the eleven axioms as a hypothesis).

*Proof.* Let $k : T \to K$ be the inclusion. First, $k$ is residually algebraic. The only prime of $K$ is $0$. An element $z \in K$ has the form $a/b$ with $a, b \in T$ and $b \neq 0$, and $p = bX - a$ has the coefficient $b$, which is nonzero in $K$, and $p(z) = 0$.

Next, $k$ has étale base change over $\mathrm{id}_T$. Let $c : T \to B$ be étale, and $Y' = K \otimes_T B$. Then $B[x]$ is étale over $T[x]$, so by fact 7 the map $B[x] \to K \otimes_T B[x] = Y'[x]$ is an equivalence. By C4 the maps $B \to B[x]$ and $Y' \to Y'[x]$ are equivalences. The composites $B \to B[x] \to Y'[x]$ and $B \to Y' \to Y'[x]$ agree, so $B \to Y'$ is an equivalence.

By induction on $n$, $k$ has étale base change over $T \to T[x_1, \dots, x_n]$ for every $n$: the case $n = 0$ is the previous paragraph, and the step is the proposition on adding a variable, since $T[x_1, \dots, x_{n+1}] \cong T[x_1, \dots, x_n][x]$ over $T$ and the property passes along isomorphisms. Fact 8 now gives the theorem. $\square$

**Remark 3.14.6 (Formalization).** The theorem `etale_base_change_of_duality` is `E3.main` applied to the eleven axioms ([EtaleDualityTraceIsomorphism.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L44)). Its name speaks of duality, but the statement has no duality in it; it is E3. Unlike E1, the statement E3 assumes $q \neq 0$. The proof of `E3.main` repeats the proof of a second statement in the same development, with all axioms of section 1 as hypotheses ([N81.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/N81.lean#L260)). The proposition on adding a variable is proved by a theorem named for strict henselizations and colimit presentations ([StrictHenselizationStalkEquivOfColimitPresentati.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/StrictHenselizationStalkEquivOfColimitPresentati.lean#L161)); its statement is the proposition. The proof of the proposition on strictly henselian pairs is in [SpSOfIntegralInjective.lean](lean:Development/EtaleCohomology/EtaleSheaves/SpSOfIntegralInjective.lean#L25). We have not unfolded the proofs of facts 4, 6 and 8; their sketches follow the names of their steps.

## Notes and references

The chapter proves the axioms E1 to E4 of section 1 from the axioms A to D, and power-sum classes and a Frobenius relation from them. [The proper base change theorem](/entry/proper-base-change/) takes E1 as an input, and other chapters of the Galois row use E2 and E3 together, for instance in [Theorem 1.2.4](/entry/es-gen-all/). All of these results lie below [the local steps](/entry/steps-holds/), which are used in the step [geometric realization of weight one](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).

M. Artin, A. Grothendieck and J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas* (SGA 4), Lecture Notes in Mathematics 269, 270 and 305, Springer, 1972 and 1973: Exposé VII, §5 for the passage to limits, Exposé XII, §5 for proper base change, Exposé XIV for finiteness, and Exposés XV and XVI for the acyclicity of smooth maps.

J. S. Milne, *Étale Cohomology*, Princeton University Press, 1980: Chapter III, Proposition 4.9 for $H^1(X, \mathbb{G}_m) = \mathrm{Pic}(X)$, and Chapter VI, §2 for proper base change and finiteness. Our treatment differs from Milne's: the properties of étale cohomology that we need are axioms, and E1 and E3 are proved from the other axioms through absolutely integrally closed rings.

O. Gabber, "Affine analog of the proper base change theorem", Israel J. Math. 87 (1994), for E1.

A. Grothendieck, "La théorie des classes de Chern", Bull. Soc. Math. France 86 (1958), 137 to 154, for Chern classes and power sums.

A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique II*, Publ. Math. IHÉS 8 (1961), Théorème 5.6.1, for Chow's lemma.

G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Princeton University Press, 1971, Chapter 7, for the congruence relation.

G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Springer, 1990, Chapter VII, for the congruence relation on Siegel modular varieties.

G. Faltings, "Crystalline cohomology and $p$-adic Galois representations", in *Algebraic Analysis, Geometry, and Number Theory*, Johns Hopkins University Press, 1989, for the comparison with crystalline cohomology.

J.-M. Fontaine, "Le corps des périodes $p$-adiques" and "Représentations $\ell$-adiques potentiellement semi-stables", in *Périodes $p$-adiques*, Astérisque 223 (1994), for the period rings and the functor $D_{\mathrm{cris}}$.
