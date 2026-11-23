---
title: Local duality, the Euler characteristic and class field theory
decls:
  - GlobalTheory.T.local_duality_class_field_facts_of_artin_tate_euler
  - GlobalTheory.langRecCore_of_artinReciprocity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local duality, the Euler characteristic and class field theory

The Selmer bounds of this chapter use three published theorems: local Tate duality, the local Euler characteristic formula and global Artin reciprocity. This section states them in the form that the proof uses. Then it proves that they give thirteen local facts about the [[Galois cohomology|9MPCZ3EAJM]] of decomposition groups, of the divisible modules $L/\mathcal{O}$ and of lattices. The facts are used in the Selmer bound at a point, [Theorem 6.2.2](/entry/selmer-bound-at-point-main/). The classical statements are recalled in [the Background on local fields](/learn/galois-cohomology/#local-fields) and [on global class field theory](/learn/class-field-theory/#global-class-field-theory).

Throughout, $\ell$ is a prime, $\overline{\mathbb{Q}}_\ell$ is an algebraic closure of $\mathbb{Q}_\ell$, and $K$ is a subfield of $\overline{\mathbb{Q}}_\ell$ of finite degree over $\mathbb{Q}_\ell$. Put $G_K = \mathrm{Gal}(\overline{\mathbb{Q}}_\ell/K)$. For $r \geq 1$ let $\chi_r : G_K \to (\mathbb{Z}/\ell^r)^\times$ be the reduction of the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules), and let $\mathbb{Z}/\ell^r(1)$ be $\mathbb{Z}/\ell^r$ with the action through $\chi_r$. For a finite $\mathbb{Z}/\ell^r$-module $M$ with a continuous action of $G_K$ (discrete topology), put $M^* = \mathrm{Hom}(M, \mathbb{Z}/\ell^r(1))$.

**Theorem 6.1.1 (Local Tate duality).** Let $K$ be finite over $\mathbb{Q}_\ell$, let $r \geq 1$ and let $M$ be a finite $\mathbb{Z}/\ell^r$-module with a continuous action of $G_K$. Then $H^2(K, \mathbb{Z}/\ell^r(1)) \cong \mathbb{Z}/\ell^r$. The cup product into this group gives maps
$$H^i(K, M) \to \mathrm{Hom}\big(H^{2-i}(K, M^*), \mathbb{Z}/\ell^r\big), \qquad i = 0, 1, 2,$$
and all of them are bijective. For $i = 1$ the map in the other variable is also bijective.

Lean: `Formalism.GaloisCohomology.LocalTateDualityK`.

This is Tate's theorem; see J.-P. Serre, *Galois Cohomology*, Chapter II, §5.2, Theorem 2. The proof takes it as an input.

**Theorem 6.1.2 (Local Euler characteristic formula).** With $K$, $r$ and $M$ as above,
$$\# H^1(K, M) = \# H^0(K, M) \cdot \# H^2(K, M) \cdot (\# M)^{[K : \mathbb{Q}_\ell]}.$$

Lean: `Formalism.GaloisCohomology.LocalEulerCharK`.

This is Serre, *Galois Cohomology*, Chapter II, §5.7, Theorem 5, for modules killed by a power of $\ell$. The proof takes it as an input.

For a number field $E$ with algebraic closure $\Omega$, let $\mathbb{A}_E^\times$ be the idele group and $G_E^{\mathrm{ab}}$ the Galois group of the maximal abelian extension of $E$ in $\Omega$. For a finite place $v$, let $\iota_v : E_v^\times \to \mathbb{A}_E^\times$ be the inclusion at $v$.

**Theorem 6.1.3 (Global Artin reciprocity).** For each number field $E$ and each algebraic closure $\Omega$ of $E$ there is a homomorphism $\mathrm{art} : \mathbb{A}_E^\times \to G_E^{\mathrm{ab}}$ with these properties.

1. $\mathrm{art}$ is continuous, surjective and open.
2. Its kernel is the closure of $E^\times \cdot (\mathbb{A}_{E,\infty}^\times)^\circ$, where $(\mathbb{A}_{E,\infty}^\times)^\circ$ is the identity component of the archimedean ideles.
3. Let $v$ be a finite place and $A$ a valuation ring of $\Omega$ over $v$. An element $g$ of $G_E^{\mathrm{ab}}$ is $\mathrm{art}(\iota_v(x))$ for a unit $x$ of $E_v$ if and only if $g$ is the image of an element of the inertia group of $A$.
4. With $v$ and $A$ as in 3, $g$ is $\mathrm{art}(\iota_v(x))$ for a uniformizer $x$ of $E_v$ if and only if $g$ is the image of $\sigma^{-1}$ for some Frobenius element $\sigma$ of $A$.
5. The closure of $\mathrm{art}(\iota_v(E_v^\times))$ is the image of the decomposition group of $A$.

Lean: `GlobalTheory.Published.GlobalArtinReciprocity` (also `GlobalTheory.HeckeGal.IsGlobalArtin`, the five properties).

This is the main theorem of [[class field theory|AA943HVK6Z]]; see J. Neukirch, *Algebraic Number Theory*, Chapter VI, and [the Background](/learn/class-field-theory/#global-class-field-theory). The proof takes it as an input.

Now let $\mathcal{O}$ be a complete discrete valuation ring, finite over $\mathbb{Z}_\ell$, with fraction field $L$. Let $\varepsilon : G \to \mathcal{O}^\times$ be a character of a profinite group $G$. A topological isomorphism $i : G \cong G_K$ is fixed whenever we speak of the cohomology of $G$ "as a local Galois group".

**Definition 6.1.4 (The local facts).** The *local facts* are the following thirteen statements.

1. (Decomposition groups.) Let $E$ be a number field and $A$ a valuation ring of $\overline{E}$ with $\ell$ in its maximal ideal. There are a finite extension $K$ of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$ and a topological isomorphism $i$ from the decomposition group $D_A$ to $G_K$. It carries cyclotomic characters to cyclotomic characters and the inertia group of $A$ onto the inertia group of $K$, and $[K : \mathbb{Q}_\ell] = [E_v : \mathbb{Q}_\ell]$ for the place $v$ under $A$.
2. (Invariant maps.) If $\varepsilon$ is cyclotomic, then $H^2(G, (L/\mathcal{O})(\varepsilon)) \cong L/\mathcal{O}$ and $H^2(G, L(\varepsilon)) \cong L$, compatibly with the projection $L \to L/\mathcal{O}$.
3. (Finiteness.) For a lattice $T$ in a representation of $G$ with its dual lattice $T'$ in the dual representation twisted by $\varepsilon$, $H^1(G, T')$ is a finitely generated $\mathcal{O}$-module.
4. (Rational duality.) In the situation of 3, if the rational invariant map is injective, each $\mathcal{O}$-linear map $H^1(G, T') \to L$ is the cup product with some class.
5. (Integral duality.) In the situation of 3, if the invariant map is injective, the cup pairing has trivial left kernel.
6. (Saturation.) In the situation of 3, each class in $H^1(G, T')$ has a nonzero multiple in the image of the cohomology of the rational dual.
7. (Naturality.) The invariant maps of 2 are natural in finitely generated topological $\mathcal{O}$-modules.
8. (Shape for a negative twist.) Let $e > 0$ and let $M \cong L/\mathcal{O}$ with $G$ acting by $\varepsilon^{-e}$. Then the locally constant classes in $H^1(G, M)$ have the shape of $(L/\mathcal{O})^{[K:\mathbb{Q}_\ell]}$ up to a finite group.
9. (Shape for the trivial twist.) The same holds for the trivial action, after dividing by the unramified classes.
10. (Unramified character.) For each place $A$ over $\ell$ there is a continuous additive map $D_A \to \mathbb{Z}_\ell$ that vanishes on inertia and takes the value $1$.
11. (Class number bound.) Let $E$ be a number field with $\ell \neq 2$ or with no real place, and let $M \cong L/\mathcal{O}$ with trivial action of $G_E$. Let $S \subseteq H^1(G_E, M)$ be a submodule of classes with locally constant cocycles that are unramified at every finite place. Then $\mathrm{length}_{\mathcal{O}}(S) \leq \mathrm{length}_{\mathcal{O}}(\mathcal{O}/\ell) \cdot v_\ell(h_E)$, where $h_E$ is the class number.
12. (Topologies.) Let $\mathcal{O}$ be a discrete valuation ring that is finite over $\mathbb{Z}_p$ and contains it. Then $\mathcal{O}$ and $L$ carry topologies for which $L$ is a topological group with continuous scalar multiplication by $\mathcal{O}$, $\mathcal{O}$ is an admissible coefficient ring, and $L$ has the expected topology.
13. (Elementary facts.) Seven elementary facts: $\mathbb{Z}_\ell$ is an admissible coefficient ring; $aM$ is open in $M$ for $a \neq 0$; quotients of continuous representations are continuous; if the cup product of two cocycles is the coboundary of a continuous cochain, their classes pair to zero; the shape of 8 is invariant under isomorphism; the ring of integers of a finite extension of $\mathbb{Q}_\ell$ is its closed unit ball; and the ring of integers is open in the field.

Lean: `ReciprocityTheory.ChartRestriction.T2.Core`.

The shape in 8 and 9 and the pairings in 3 to 6 are the ones of the lattice cohomology of this volume. We do not need their exact form below: the next section uses the local facts as one input.

**Theorem 6.1.5 (The local facts).** Assume global Artin reciprocity, local Tate duality and the local Euler characteristic formula. Then the thirteen local facts hold.

Lean: `GlobalTheory.langRecCore_of_artinReciprocity` (also `GlobalTheory.T.local_duality_class_field_facts_of_artin_tate_euler`, a second name).

*Proof.* We prove each fact from its own lemma. Facts 1, 6, 10, 12 and 13 need none of the three inputs. Fact 1 identifies the decomposition group with the Galois group of the completion. Fact 10 is the composite of $D_A \to D_A/I_A \cong \widehat{\mathbb{Z}}$ with the projection $\widehat{\mathbb{Z}} \to \mathbb{Z}_\ell$, evaluated on a Frobenius. Facts 2, 3, 4, 5 and 7 come from local Tate duality: the invariant map for $\mathbb{Z}/\ell^r(1)$ passes to the limit and gives 2 and 7, and the perfectness of the cup products on finite levels gives the finiteness 3, the rational duality 4 and the integral duality 5. Facts 8 and 9 come from local Tate duality and the Euler characteristic formula together. The formula gives the order of $H^1$ at each finite level, and duality gives $H^0$ and $H^2$ of a nontrivial twist, so the length of $H^1(K, \ell^{-n}\mathcal{O}/\mathcal{O}(\varepsilon^{-e}))$ grows like $n [K : \mathbb{Q}_\ell]$ times the length of $\mathcal{O}/\ell$. Fact 11 comes from global Artin reciprocity. A class in $S$ is a homomorphism $G_E \to M$ that is trivial on all inertia groups. By 1 to 5 of reciprocity it factors through the Galois group of the Hilbert class field, which is $\mathrm{Cl}_E$; the condition at the real places is empty when $E$ has none, and is harmless when $\ell \neq 2$. So $S$ embeds in $\mathrm{Hom}(\mathrm{Cl}_E, M)$, whose length is at most $\mathrm{length}(\mathcal{O}/\ell) \cdot v_\ell(h_E)$. $\square$

**Remark 6.1.6 (Formalization).** The thirteen facts are the fields of `ReciprocityTheory.ChartRestriction.T2.Core` in [LatDefs.lean](lean:ReciprocityTheory/ReductiveGroups/TraceFormulas/LatDefs.lean#L319). The theorem name says "langRecCore" but the conclusion is this record, not a statement of local Langlands. The saturation fact (`JSpan`, line 235) has no hypothesis that $K$ is finite over $\mathbb{Q}_\ell$, unlike its neighbours. We have not unfolded `QuotShape`, `HcLC`, `NatInv`, `LatData` or `RealLatG`, so facts 3 to 9 are stated above in words only. We did not open the proofs of the thirteen lemmas; the proof above gives the dependence on the three inputs that the Lean terms show, and the classical argument for each. The second name is proved by `first | exact ...` in a file with `maxHeartbeats 1000000`.
