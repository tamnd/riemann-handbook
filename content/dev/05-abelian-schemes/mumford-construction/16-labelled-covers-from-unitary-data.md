---
title: Labelled covers from unitary data
decls:
  - GlobalTheory.Mum.exists_desc_labels
  - GlobalTheory.T.exists_labelledSemiAbelianCover_finite_extension
  - GlobalTheory.Mum.UCover.labCover
  - GlobalTheory.T.nonempty_labelled_cover_of_odd_prime
  - GlobalTheory.Mum.exists_labCover_of_pelOK
  - GlobalTheory.T.exists_labelledCover_unitaryPELType_finiteExt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Labelled covers from unitary data

This section proves that degeneration data of unitary PEL type have a [labelled cover](/entry/has-fin-of-lab-cover/) after a finite extension of the base. [Mumford's construction](/entry/has-of-base/) uses this as the step from the unitary data to a semi-abelian scheme over a modification. The proof starts from Mumford's construction over one complete trait, which gives an abelian variety with a symmetry condition. It descends the abelian variety and labels of its torsion to a finite extension of the base. Then it extends the abelian variety to a semi-abelian scheme over a modification, and checks the trait condition with [the recognition theorem of the previous section](/entry/pull-deg-induces/).

Throughout, $R$ is a base with fraction field $K$, and we use labels, fibres of polarised abelian varieties, labels correct at one trait and Galois equivariant labels as in [the previous section](/entry/pull-deg-induces/).

### Two conditions

**Definition 4.16.1 (Condition (S)).** Let $G$ be a commutative group scheme over a scheme $B$ and $L$ a line bundle on $G$. The pair $(G, L)$ satisfies *condition (S)* if there are homomorphisms $w, w^\dagger : G \to G$ with $w + w^\dagger = 1$ and generating isomorphisms
$$
\begin{aligned}
L &\cong (1, w)^* \Lambda(L), \\
(w \times 1)^* \Lambda(L) &\cong (1 \times w^\dagger)^* \Lambda(L).
\end{aligned}
$$
Here $\Lambda(L)$ is the Mumford bundle, with fibre $L_{x+y} \otimes L_x^{-1} \otimes L_y^{-1} \otimes L_0$ at $(x, y)$.

Lean: `GlobalTheory.ZH.HypS`.

The second isomorphism says that $w^\dagger$ is the adjoint of $w$ for the polarisation of $L$. The first says that $L$ is the pullback of the Mumford bundle along the graph of $w$. A polarised abelian variety $A$ *satisfies condition (S)* if $(A, L_A)$ does. Data of unitary PEL type give such a $w$ through the action of the ring of integers of the CM field.

**Definition 4.16.2 (Uniformised cover).** A *uniformised cover* of $\operatorname{Spec} R$ consists of the following data.

1. A modification $(S, \pi, \gamma)$ of $\operatorname{Spec} R$.
2. A commutative semi-abelian scheme $G$ over $S$ with a cubical symmetric line bundle $P$.
3. A polarised abelian variety $A$ over $K$, a morphism $\alpha : A \to G$ that makes $A$ the group pullback of $G$ along $\gamma$, and a generating isomorphism $L_A \cong \alpha^* P$.
4. The trait condition. Let $W$ be a complete trait, $\varphi : R \to W$ an injective map and $\xi$ a trait of $S$ over $\varphi$. Then there are a complete trait $W'$ with a finite injective map $\iota : W \to W'$, a commutative group scheme $G'$ over $W'$ with a morphism $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $\xi \circ \operatorname{Spec} \iota$, degeneration data $D'$ over $W'$, and a uniformisation $U'$ of $(A', G')$ by $D'$ with a generating isomorphism $L_{U'} \cong \beta^* P$.

Lean: `GlobalTheory.Mum.UCover`.

A uniformised cover is a labelled cover without the data $D$ and without the labels. Its trait condition asks only for some uniformisation at each trait, with no link to fixed data, and $\varphi$ need not be local.

**Definition 4.16.3 (Uniformised trait).** Let $D$ be degeneration data over $R$ and $A$ a polarised abelian variety over $K$. We say that $(D, A)$ has a *uniformised trait* if there are a complete trait $W$, an injective local map $\varphi : R \to W$, a commutative semi-abelian scheme $G'$ over $W$, data $D'$ over $W$ with a structure of pullback of $D$ along $\varphi$, a uniformisation of $(A', G')$ by $D'$, and a morphism $a : A' \to A$ that makes $A'$ a fibre of $A$ over $\varphi$.

Lean: `GlobalTheory.Mum.UniTrait`.

This is the definition of labels correct at one trait, without the labels.

### A labelled cover from a uniformised cover

**Theorem 4.16.4 (Labelled cover from a uniformised cover).** Let $R$ be a base, $D$ degeneration data over $R$, $C$ a uniformised cover of $\operatorname{Spec} R$ with abelian variety $A$, and $(\ell_k)$ labels of $D$ in $A$. Let $n$ be an odd prime that is a unit in $R$. If the labels are correct at one trait and Galois equivariant at the powers of $n$, then $D$ has a labelled cover.

Lean: `GlobalTheory.Mum.UCover.labCover` (also `GlobalTheory.T.nonempty_labelled_cover_of_odd_prime`, a second name).

*Proof.* We take the modification, $G$, $P$, $A$ and $\alpha$ from $C$, the prime $n$, and the labels $\ell_{n^j}$ at level $n^j$. It remains to check the trait condition. Let $W$ be a complete trait, $\varphi : R \to W$ an injective local map and $\xi$ a trait of $S$ over $\varphi$.

*Step 1: the uniformisation.* The trait condition of $C$ gives $W'$, $\iota$, $G'$, $\beta$, $D'$, $A'$ and $U'$ with $L_{U'} \cong \beta^* P$. The map $\iota$ is local, since it is finite and injective. The scheme $G'$ is semi-abelian, since it is a group pullback of a semi-abelian scheme.

*Step 2: the generic fibre.* Through $U'$, the abelian variety $A'$ is the generic fibre of $G'$. So the composite $A' \to G' \to G$ makes $A'$ the group pullback of $G$ along $\operatorname{Spec} \operatorname{Frac} W' \to \operatorname{Spec} W' \to S$. This map lies over $\operatorname{Spec}$ of the injective map $R \to \operatorname{Frac} W'$. By an input on modifications, it factors through the generic point $\gamma$ by a field map $g : K \to \operatorname{Frac} W'$ that extends $\iota \circ \varphi$.

*Step 3: the fibre map.* Since $\alpha$ makes $A$ the group pullback of $G$ along $\gamma$, there is a unique $a : A' \to A$ with $\alpha \circ a$ equal to the composite of Step 2 and with $a$ over $\operatorname{Spec} g$. Cancelling the pullback square of $\alpha$, $a$ makes $A'$ the group pullback of $A$ along $\operatorname{Spec} g$. For the line bundles,
$$
L_{A'} \cong L_{U'}|_{A'} \cong (\beta^* P)|_{A'} \cong a^* \alpha^* P,
$$
and $\alpha^* P \cong L_A$. So $L_{A'} \cong a^* L_A$, and $a$ makes $A'$ a fibre of $A$ over $\iota \circ \varphi$.

*Step 4: recognition.* The map $\iota \circ \varphi$ is injective and local. By [the theorem on recognition at every trait](/entry/pull-deg-induces/), there is a structure of pullback of $D$ along $\iota \circ \varphi$ on $D'$, such that the labels induce $U'$ at every level $n^j$.

*Step 5: the labels.* Let $F$, the embedding $e$, the classes $p, p'$ and the point $x' \in A'(F)$ be as in the trait condition of a labelled cover, so that $x'$ lies over the image of $\ell_{n^j}(p)$ in $G$. Both $a(x')$ and $e(\ell_{n^j}(p))$ map to the same point of $G$ under $\alpha$. The map $\gamma$ is a monomorphism, since $\operatorname{Spec} K \to \operatorname{Spec} R$ is one and $\pi \circ \gamma$ is this map. So $\alpha$, a pullback of $\gamma$, is a monomorphism too, and $a(x') = e(\ell_{n^j}(p))$. By Step 4, $U'$ carries $p'$ to $x'$. $\square$

### Labels after a finite extension

**Theorem 4.16.5 (Labelled abelian variety after a finite extension).** Let $R$ be a base, $D$ degeneration data over $R$ and $n$ an odd prime that is a unit in $R$. Let $W$ be a complete trait and $\varphi : R \to W$ an injective local map. Let $D'$ be data over $W$ that are a pullback of $D$ along $\varphi$, $G'$ a commutative semi-abelian scheme over $W$, and $A'$ a polarised abelian variety over $\operatorname{Frac} W$ that satisfies condition (S), such that $(A', G')$ has a uniformisation by $D'$. Then there are a finite extension $\rho : R \to R_1$, data $D_1$ over $R_1$ that are a pullback of $D$ along $\rho$, a polarised abelian variety $A$ over $\operatorname{Frac} R_1$ that satisfies condition (S), and labels of $D_1$ in $A$ that are correct at one trait and Galois equivariant at the powers of $n$.

Lean: `GlobalTheory.Mum.exists_desc_labels` (also `GlobalTheory.T.exists_labelledSemiAbelianCover_finite_extension`, a second name).

*Proof.* *Step 1: the geometric fibre.* By an input, there are a polarised abelian variety $A_0$ over $\bar K$ that satisfies condition (S), and an embedding $e_0 : \bar K \to \overline{\operatorname{Frac} W}$ that agrees with $\varphi$ on $R$, such that $A_0$ and $A'$ become isomorphic as polarised abelian varieties over $\overline{\operatorname{Frac} W}$. So $A'$ is defined over $\bar K$, up to geometric isomorphism.

*Step 2: a finite extension.* By a second input, $A_0$ and the uniformisation descend to a finite level: there are a finite extension $\rho : R \to R_1$, a pullback $D_1$ of $D$ along $\rho$, and a polarised abelian variety $A$ over $\operatorname{Frac} R_1$ that satisfies condition (S), such that $(D_1, A)$ has a uniformised trait.

*Step 3.* The ring $R_1$ is a base: it is an admissible base, and it has characteristic $0$ since $\rho$ is injective.

*Step 4: labels.* By a third input, a uniformised trait gives labels of $D_1$ in $A$ that are correct at one trait. They are read off from the good labelling of the uniformisation.

*Step 5: equivariance.* By a fourth input, after one more finite extension of $R$ the labels become Galois equivariant at the powers of $n$, and the other properties are kept. This gives the conclusion. $\square$

### The unitary case

**Lemma 4.16.6 (A small odd prime).** In every local ring, $3$ or $5$ is a unit.

Lean: `GlobalTheory.Mum.exists_odd_prime_isUnit_in_localRing`.

*Proof.* We have $2 \cdot 3 - 5 = 1$. If $3$ and $5$ were both in the maximal ideal, then $1$ would be in it. $\square$

**Theorem 4.16.7 (Labelled cover for unitary data).** Let $R$ be a base, $E$ a CM field with host data and a unitary datum, and $D$ degeneration data over $R$ with an action of $\mathcal{O}_E$ on its character lattice $\mathsf{X}$ of unitary PEL type. If $\mathsf{X} \neq 0$, then there are a finite extension $\rho : R \to R'$ and data $D'$ over $R'$ that are a pullback of $D$ along $\rho$, such that $D'$ has a labelled cover.

Lean: `GlobalTheory.Mum.exists_labCover_of_pelOK` (also `GlobalTheory.T.exists_labelledCover_unitaryPELType_finiteExt`, a second name).

*Proof.* *Step 1: the prime.* By the lemma, there is an odd prime $n \in \{3, 5\}$ that is a unit in $R$.

*Step 2: a trait.* By an input, there are a complete trait $V$ and an injective map $\varphi : R \to V$ with $\varphi^{-1}(\mathfrak{m}_V) = \mathfrak{m}$. So $\varphi$ is local: an element of $R$ that is not a unit lies in $\mathfrak{m}$, so its image lies in $\mathfrak{m}_V$.

*Step 3: the data at the trait.* Let $D_V$ be a pullback of $D$ along $\varphi$. It is again of unitary PEL type, and its character lattice is isomorphic to $\mathsf{X}$, so it is non-zero.

*Step 4: Mumford's construction at the trait.* By an input on data of unitary type over a complete trait, there are a complete trait $V'$ with a finite injective map $\iota : V \to V'$, a pullback $D'$ of $D_V$ along $\iota$, a commutative semi-abelian scheme $G'$ over $V'$, and a uniformisation of $(A', G')$ by $D'$, where $A'$ satisfies condition (S). Then $D'$ is a pullback of $D$ along $\iota \circ \varphi$, which is injective and local.

*Step 5: labels.* The previous theorem, at the trait $\iota \circ \varphi$, gives a finite extension $\rho_1 : R \to R_1$, a pullback $D_1$ of $D$, a polarised abelian variety $A$ over $\operatorname{Frac} R_1$ with condition (S), and labels of $D_1$ in $A$ that are correct at one trait and Galois equivariant at the powers of $n$. The ring $R_1$ is a base.

*Step 6: a uniformised cover.* By an input, a polarised abelian variety with condition (S) over the fraction field of a base has a uniformised cover after a finite extension: there are a finite extension $\rho_2 : R_1 \to R_2$, a uniformised cover $C$ of $\operatorname{Spec} R_2$ with abelian variety $A_C$, and $a : A_C \to A$ that makes $A_C$ a fibre of $A$ over $\rho_2$. The ring $R_2$ is a base.

*Step 7: moved labels.* Let $D_2$ be a pullback of $D_1$ along $\rho_2$. By an input, the labels move along $a$ to labels of $D_2$ in $A_C$ that are correct at one trait and Galois equivariant at the powers of $n$.

*Step 8.* The prime $n$ is a unit in $R_2$. By the theorem on labelled covers from uniformised covers, $D_2$ has a labelled cover. The composite $\rho_2 \circ \rho_1$ is a finite extension, and $D_2$ is a pullback of $D$ along it. $\square$

**Remark 4.16.8 (Formalization).** The second names are wrappers. In the first theorem ([NonemptyLabelledCoverOfOddPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NonemptyLabelledCoverOfOddPrime.lean#L38)), Step 1 uses `GlobalTheory.Mum.CoverFin.semiAbelian_of_pull`, Step 2 uses `GlobalTheory.ThetaBaseChange.grp_generic` and the input `GlobalTheory.T.exists_factor_field_point_through_generic_point`, and the monomorphism of Step 5 is `GlobalTheory.Mum.UCoverLab.mono_α`. The locality of $\varphi$ is used only to apply the recognition theorem, at line 85. In the second theorem ([ExistsLabelledSemiAbelianCoverFiniteExtension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledSemiAbelianCoverFiniteExtension.lean#L22)), Steps 1, 2, 4 and 5 are `GlobalTheory.T.exists_geometricFibreIso_of_traitUniformisation` (with `GlobalTheory.Mum.GeomIso`), `GlobalTheory.T.exists_uniformisedTrait_descent_finite_ext`, `GlobalTheory.T.exists_torsionLabels_uniformisedDominatingTrait` and `GlobalTheory.T.exists_finite_extension_galois_equivariant_labels`; the ring of the conclusion is the one returned by the last input, not the $R_1$ of Step 2, and the prime $n$ is only passed through to the inputs. In the last theorem ([ExistsLabelledCoverUnitaryPELTypeFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledCoverUnitaryPELTypeFiniteExt.lean#L35)), Steps 2 to 7 use `GlobalTheory.PrimeUnif.exists_cdvr`, `GlobalTheory.MumPull.exists_pull`, `GlobalTheory.Mum.pelOK_of_isPullDeg`, `GlobalTheory.T.exists_mumfordUniformisation_unitaryTypeTrait`, `GlobalTheory.T.exists_uniformised_cover_finite_ext_of_symmetric` and `GlobalTheory.T.exists_torsionLabels_finiteExtension_galoisEquivariant`. We did not open the proofs of these inputs, and the reasons given for them are sketches. The Mumford bundle in condition (S) is written in the code as `cubeLB` of a pair of maps.
