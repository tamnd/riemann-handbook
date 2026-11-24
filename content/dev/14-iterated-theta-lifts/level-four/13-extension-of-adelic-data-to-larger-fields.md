---
title: Extension of adelic data to larger fields
decls:
  - GlobalTheory.T.adelicData_extend_largerFields_of_hypotheses
  - GlobalTheory.Mem.R3.Rw.datExt0_of_hypotheses
  - GlobalTheory.T.exists_extendedColumnData_all_clauses_but_places
  - GlobalTheory.Mem.R3.Rw.ExtBuild.exists_ext_build
  - GlobalTheory.T.exists_extendedAdelicData_with_intertwiners_over_enlargedCore
  - GlobalTheory.Mem.R3.Rw.datExt_rest
  - GlobalTheory.T.geometricHalf_to_analyticData_enlargedBase
  - GlobalTheory.T.extendedData_nonzero_index_places_correspond_alt
  - GlobalTheory.Mem.R3.TwistedPlaceExtensions.extendedData_nonzero_index_places_correspond
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Extension of adelic data to larger fields

The construction enlarges the base many times: the coefficient field grows, and new primes enter the twist data. Each fine adelic datum over the old base must then extend to a fine adelic datum over the new base. In this section we prove this extension. The proof has two parts. The first builds the new datum with all its clauses except the clause on the places. The second shows that the places where the local index is nonzero correspond under the enlargement. The result enters [the large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/).

### Enlargements and extensions

A base $B$ has a pre-base, a field $K_s$ with an image in the coefficient field, a lattice $L_{B,0}$ and an embedding of lattices. We use the column steps of [Section 1.8.4](/entry/step-w-core/).

**Definition 1.13.1 (Enlargement with fixed coefficient field).** A base $B'$ is an enlargement of $B$ with the same pre-base if $B$ and $B'$ have the same pre-base and the same image of $K_s$, the image of $L_{B,0}$ lies in the image of $L_{B',0}$, and the range of the embedding of lattices of $B$ lies in that of $B'$.

An adelic datum $z$ over a stage has a core, an algebra structure and the analytic and geometric data at each place. It is fine if it is exact at its places, has geometry, has a core and is standard. For an adelic datum and a context, a place $v$ is in the set $W_1$ if $v$ or its conjugate has a nonzero local datum for some $j$: the local index is nonzero, or the twist $j_w$ is nonzero, or the field $F_0$ is nonzero at $v$.

**Definition 1.13.2 (Extension).** Let $z$ be an adelic datum over $B$ and $z'$ one over an enlargement $B'$. Then $z'$ extends $z$ without places if the core of $z'$ is the transport of the core of $z$ and each local datum of $z'$ is the image of that of $z$ under the enlargement. It extends $z$ if, in addition, for all places $v$ of $B$ and $v'$ of $B'$ such that $v'$ lies over $v$ (the two embeddings agree), $v \in W_1(z)$ if and only if $v' \in W_1(z')$.

**Definition 1.13.3 (Extension of adelic data).** The extension property is the column step from "pinned" to the following. For every enlargement $B'$ of $B$ with the same pre-base, frame $f'$ and twist data $T'$, the frames and the pins being equal, and for every stage $Z$ with a fine adelic datum $z$ whose groups are true and fit, and every stage $Z'$ over $B'$ whose groups are true, fit and have tied volumes, there is a fine adelic datum $z'$ over $Z'$ with places $\{v : \text{the residue characteristic of } v \text{ is in the prime set of } T'\}$ that extends $z$.

**Theorem 1.13.4 (Extension of adelic data).** Assume (DS) the cover of the discrete series by the parameters, (HC) the theory of Harish-Chandra modules, (RD) rapid decay of cusp forms, (CW) the Casselman-Wallach theorem, (WU) the Weil representation of a unitary dual pair, (DE) the existence of the discrete series of $U(p,q)$, and (HF) the finiteness theorem of Harish-Chandra. Then the extension property holds.

Lean: `GlobalTheory.Mem.R3.Rw.datExt0_of_hypotheses` (also `GlobalTheory.T.adelicData_extend_largerFields_of_hypotheses`, a second name).

*Proof.* The theorem on extension without places below gives, under the seven hypotheses, a fine $z'$ that extends $z$ without places. The theorem on nonzero index places gives the clause on the places for the same $z'$. Together they give an extension. $\square$

### The construction without places

**Theorem 1.13.5 (Extension without places).** Assume the seven hypotheses of the previous theorem. Then the extension property holds with "extends without places" in place of "extends".

Lean: `GlobalTheory.Mem.R3.Rw.ExtBuild.exists_ext_build` (also `GlobalTheory.T.exists_extendedColumnData_all_clauses_but_places`, a second name).

*Proof.* The core of $z$ transports to a core $c'$ over the enlarged coefficient base. The transport gives an algebra structure, three algebra facts, the identification of each part of the core, and four laws. The theorem on the rest of the datum below, applied to $c'$, gives an adelic datum $z'$ over $Z'$ with core $c'$, exact at its places, with geometry and standard, which extends $z$ without places. The core of $z'$ is $c'$, so $z'$ has a core, and $z'$ is fine. $\square$

**Theorem 1.13.6 (Rest of the datum).** Assume the seven hypotheses. Let $z$ and $Z'$ be as in the extension property, and let $c'$ be the transported core with its laws. Then there is an adelic datum $z'$ over $Z'$ with core $c'$, exact at its places, with geometry, standard, and which extends $z$ without places.

Lean: `GlobalTheory.Mem.R3.Rw.datExt_rest` (also `GlobalTheory.T.exists_extendedAdelicData_with_intertwiners_over_enlargedCore`, a second name).

*Proof.* The analytic data over the enlarged base exist without the tuples, and the characterised data exist for the Weil representation over the enlarged base. The image of the Weil group $W_K$ under the twist of the place is given by an embedding $\iota$ when a compatible one exists. The theorem on the geometric half below gives the geometric data. The three parts together give $z'$. $\square$

**Theorem 1.13.7 (Geometric half over the enlarged base).** Assume rapid decay of cusp forms. Let $z$ be an adelic datum over $B$ with geometry, and let $B'$ be an enlargement. Then there is a geometric half over the enlarged base with geometry, whose place $v_0$, index $j$, constants $\kappa$ and coordinates agree with those of $z$ under the ring map $\iota$ of the enlargement.

Lean: `GlobalTheory.T.geometricHalf_to_analyticData_enlargedBase`.

*Proof.* The ring map $\iota$ comes from the embedding of the enlargement. Geometry passes along a column step. A field map with the right values exists at the place $v_0$, and an extension of the forms over $\iota$ exists. The ties of the enlargement carry the coordinates of $z$ to those of the new half. $\square$

### Places with nonzero index

For a place $P$ of a number field $K$ and two finitely generated lattices $A$, $B$ in $K^n$, let $\mathrm{lidx}_P(A, B)$ be the local index of $B$ in $A$ at $P$ (see [discrete valuation rings and lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices)).

**Lemma 1.13.8 (Index under a field map).** Let $\varphi : K \to K'$ be a map of number fields, $G$ an invertible matrix over $K'$, and $P$, $P'$ places of $K$ and $K'$ with $P'$ over $P$. Then for finitely generated lattices $A$ and $B$,
$$\mathrm{lidx}_P(A, B) \neq 0 \iff \mathrm{lidx}_{P'}\big(\langle G\varphi(A)\rangle, \langle G\varphi(B)\rangle\big) \neq 0.$$

This lemma is a second name of the local index lemma for base change, and we use it as given.

**Theorem 1.13.9 (Nonzero index places correspond).** Assume the seven hypotheses. Let $z$ be a fine adelic datum over $B$ and $z'$ a fine adelic datum over an enlargement that extends $z$ without places. Then for all places $v$ of $B$ and $v'$ of $B'$ over $v$, $v \in W_1(z)$ if and only if $v' \in W_1(z')$.

Lean: `GlobalTheory.Mem.R3.TwistedPlaceExtensions.extendedData_nonzero_index_places_correspond` (also `GlobalTheory.T.extendedData_nonzero_index_places_correspond_alt`, a second name).

*Proof.* The lifted lattice of the forms and the definite lift lattice change by base change along the enlargement, with invertible matrices $G$ and $N$. A place $v$ is in $W_1(z)$ if its local datum is nonzero at $v$ or at its conjugate. The twist $j_w$ and the field $F_0$ are nonzero at $v$ if and only if they are nonzero at $v'$, because the extension maps the local data. The local index is nonzero at $v$ if and only if it is nonzero at $v'$, by the lemma on the index under a field map. The dual lattice of a Hermitian lattice commutes with base change, so the same holds for the index of the dual. A place over the conjugate of $v$ is the conjugate of a place over $v$. $\square$

**Remark 1.13.10 (Formalization).** In [GeometricHalfToAnalyticDataEnlargedBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/GeometricHalfToAnalyticDataEnlargedBase.lean#L56) only `CuspRapidDecay` of the seven hypotheses is used, and at line 58 the hypothesis on the image of $W_K$ is discarded. So the lemma `wk_image` that `datExt_rest` supplies has no effect ([ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedAdelicDataWithIntertwinersOverEnla.lean#L29)); `wk_image` is also vacuous, with the value $0$, when no compatible $\iota$ exists. The second name of `datExt_rest` says "with intertwiners", but no intertwiner appears in the statement. The second name of `exists_ext_build` says "column data", but the object is an adelic datum. The lemma on the index is `lattice_index_nonzero_iff_under_field_map`, a second name of `LidxBaseChange.lidx_ne_zero_iff` ([LatticeIndexNonzeroIffUnderFieldMapStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LatticeIndexNonzeroIffUnderFieldMapStatement.lean#L7)). The extension property is `DatExt0` and the enlargement is `Enl0` ([IsBaseEnlargementFixedCoefFieldOfCoeffEnlargemen.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsBaseEnlargementFixedCoefFieldOfCoeffEnlargemen.lean#L22)).
