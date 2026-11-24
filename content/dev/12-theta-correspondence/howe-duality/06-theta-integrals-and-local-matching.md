---
title: Theta integrals and local matching
decls:
  - PositivityTheory.ThKR.theoremK_head2_of_mod
  - PositivityTheory.ThKR.theoremK_head2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta integrals and local matching

This section proves the two theta statements used by the [theta matching chapter](/proof/theta-matching/): that global theta integrals into one unitary group agree up to a nonzero constant, and that the local Weil representations at each place have matched quotients. Both follow from two analytic inputs, the continuation of Siegel [[Eisenstein series|3NZBZXYWAJ]] and the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula), once the local results of the previous sections are put in place. The result is passed by the [literature step](/step/theta-integrals-agree-and-local-matching-of-literature/), which supplies the two inputs, to the theta matching chapter, where the two conclusions are its inputs on theta integrals and on local matching.

### The statements

We work with a CM extension $E/F$, a Hermitian space $X$ of dimension $n$ and a skew-Hermitian space $W$ of dimension $d$ over $E$, a standard additive character $\psi$, and the [Weil representations](/entry/s-weil-ex/) of the previous section. The theta integral of a Schwartz function $\Phi$ against $h \in U(W)(\mathbb{A})$ is
$$I(\Phi)(h) = \int_{U(X)(F) \backslash U(X)(\mathbb{A})} \theta(g, h; \Phi)\, dg,$$
where $\theta(g, h; \Phi) = \sum_{x} \omega(g, h) \Phi(x)$ is the [theta kernel](/learn/theta/#theta-kernels).

**Definition 2.6.1.** The statement *theta integrals agree* says: for each admissible triple, the theta integrals converge and decay; two theta integrals into the same $U(W)$ with matching test functions are proportional with one nonzero constant; and these constants satisfy two recursion laws in the dimension. The statement *local matching* says: at each place $v$, the two local Weil representations attached to the triple have quotient maps onto one irreducible representation of $U(W)(F_v)$, and the maps are compatible. Both are unfolded in their steps, [theta integrals agree](/step/theta-integrals-agree-def/) and [local matching](/step/local-matching-def/).

**Definition 2.6.2.** The statement *Eisenstein continuation* says that the Siegel Eisenstein series $E(s)$ of the doubled unitary group converges and is holomorphic for $\operatorname{Re} s$ large, and that near each $s_0$ there are $k \geq 0$ and functions $H(s)$ of moderate growth with
$$H(s) = (s - s_0)^k E(s) \qquad (s \neq s_0),$$
such that $\mu(H(s))$ is holomorphic near $s_0$ for every linear form $\mu$ that is bounded on each growth class. The statement *Siegel-Weil* is the standard [Siegel-Weil formula](/proof/siegel-weil/) for the doubled pair: the theta integral of a test function in the doubled Weil representation is a constant multiple of the value of the Siegel Eisenstein series at the corresponding point.

**Definition 2.6.3.** Let $v$ be a finite place of $F$ inert in $E$, let $W$ have dimension $d = 2m$ with a lattice $L_v$, and let $Y$ be a Lagrangian at $v$ adapted to $L_v$, so that $L_v = (L_v \cap Y) + (L_v \cap Y')$ for a complementary Lagrangian $Y'$. Let $P$ be the stabilizer of $Y$ in $U(W)(F_v)$, $K$ the stabilizer of $L_v$ and $K_P = P \cap K$. For $p \in P$ let $t$ be the matrix of $p$ on $Y$ and $u = N_{E_v/F_v}(\det t)$. The *modulus identity* says
$$[K_P : K_P \cap p^{-1} K_P p] = |u|_v^{m}\, [K_P : K_P \cap p K_P p^{-1}],$$
where $|u|_v$ is the factor by which multiplication by $u$ scales a [[Haar measure|CE0V9686M8]] of $F_v$.

The modulus identity is the index form of the statement that the modular character of $P$ is $|N \det t|^{m}$; see [Haar measure](/learn/analysis/#haar-measure). It is proved in the [entry on the modulus identity](/entry/mod-st2/).

### The theorem with the modulus identity as input

**Theorem 2.6.4 (Theta integrals and local matching, from the modulus identity).** If the modulus identity, Eisenstein continuation and the Siegel-Weil formula hold, then theta integrals agree and local matching holds.

Lean: `PositivityTheory.ThKR.theoremK_head2_of_mod`

*Proof.* Apply the [assembly theorem](/entry/close-sph/) of the theta series chapter, which derives both conclusions from fourteen local and global inputs. They are supplied as follows.

1. *Ramified and split finite places.* The local quotient maps at the places of the ramification set and at the split places outside it, the coinvariant statements for the compact open subgroups, and [multiplicity one at ramified places](/entry/ramified-multiplicity-one/) all come from one geometric lemma on filtrations of induced representations.
2. *Spherical or irreducible.* At each place, each of the two local Weil representations is spherical or irreducible. This comes from the split case of the spherical theory and from the lattice vacua of [Howe duality at the inert places](/entry/howe-inert/).
3. *Inert places.* The local quotient maps at the inert places outside the ramification set are built from the lattice vacua, from the existence of local representations, and from the [spherical functions](/entry/sph-fun-of-mod-st/) of the theta series chapter, which use the modulus identity. This is the only use of the modulus identity.
4. *Infinite places.* The [Lie action of the second member](/entry/lie-second2/) of the previous section, the corresponding statement for the first member and the description of the lowest $K$-types at the real places all come from one theorem on local lifts of one-parameter subgroups of $\mathfrak{sp}_{2l}(\mathbb{R})$ to the Schwartz space, together with the derivatives of Heisenberg lines.
5. *Global inputs.* Reduction theory gives Siegel sets for the unitary group; the [existence of Weil representations](/entry/s-weil-ex/) is the theorem of the previous section; and Eisenstein continuation and the Siegel-Weil formula are the two hypotheses.

With all fourteen inputs supplied, the assembly theorem gives the two conclusions. $\square$

### Removing the modulus identity

**Theorem 2.6.5 (Theta integrals and local matching).** If Eisenstein continuation and the Siegel-Weil formula hold, then theta integrals agree and local matching holds.

Lean: `PositivityTheory.ThKR.theoremK_head2`

*Proof.* The modulus identity holds for every number field and all such data, by the [theorem on the modulus identity](/entry/mod-st2/). Apply the previous theorem. $\square$

In the proof of the main theorem both remaining hypotheses are theorems: the literature step supplies Eisenstein continuation from the theory of [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) and the Siegel-Weil formula from the [Siegel-Weil chapter](/proof/siegel-weil/). So the two theta statements hold with no hypothesis. In the classical literature the theta integral identity is the global part of the [doubling method](/learn/theta/#the-doubling-method) and of the [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula), and local matching is the local theta correspondence for the places at hand; the next section treats the Rallis inner product.

**Remark 2.6.6 (Formalization).** Both theorems are in [TheoremKOfMod.lean](lean:Development/WeilBound/ThetaLifts/Reductions/FiniteClosure/TheoremKOfMod.lean#L14), the first at L14 and the second at L26. The names "Theorem K" and "head2" do not describe the statements. The same file has a third theorem at L22 with an extra hypothesis `_P` that its proof does not use. The infinite places use two proofs of the same derivative statement: one passed to the Lie theorem directly, and another used inside the proof of the lowest $K$-type statement. The modulus identity `ModSt` is stated with relative indices of subgroups in [FunDefs.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/FunDefs.lean#L98).
