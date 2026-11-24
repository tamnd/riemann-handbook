---
title: Labels and the reduction of the compact group
decls:
  - GlobalTheory.LabPin.frameRed_exists
  - GlobalTheory.T.exists_maximalCompact_reduction_standardFrame
  - GlobalTheory.LabPinTop.labTie_of_series
  - GlobalTheory.T.labels_fixed_by_tupleOperator_of_typeSeries
  - GlobalTheory.LabPinAt.labTie_at
  - GlobalTheory.T.realisationLabels_normalised_of_rowsTypes_levels
  - GlobalTheory.Sat.ties_at
  - GlobalTheory.T.constructedSpectralObjects_irreducibilityConditions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Labels and the reduction of the compact group

This section proves the label tie for the spectral rows of a datum: each row vector is fixed by the operator of its label tuple. The proof reduces the maximal compact subgroup at the type places to a finite group of matrices, and it uses the series idempotents of the types at these places. The label tie, with the automorphic tie and the row dictionary tie, is the conclusion of the last theorem here. These three ties are used by [the ties of the realisation data](/entry/ties-of-n-at-data-real/) and by the irreducibility row of the fifteenth section.

### The finite reduction

Let $D$ be a datum of rank $r$ with type primes $g_0 \ne g_1$, and let $X$ be a Hida setting for $D$ whose instance is the instance of $D$ and whose map of CM fields is the identity. For $k \in \{0, 1\}$ let $\mathrm{Pl}_k$ be the chosen places over $g_k$, one in each conjugate pair. The *finite level group* is
$$G_0 = \prod_{k} \prod_{v \in \mathrm{Pl}_k} \mathrm{GL}_r(\mathbb Z / g_k).$$
At a split place $s$ of $E$ over the place $v$, a finite adelic point $x$ is a *lift* of $\gamma \in \mathrm{GL}_r(\mathbb Z/g_k)$ if $x$ is trivial outside $s$ and each entry of $x_s - \gamma$ has valuation less than $1$.

Let $t$ be an adelic point and let $\psi_Y$ be a row character datum: a map from the compact group of the space $Y_0$ to the adelic group. A *frame reduction* is a point $c$ and a map $\mathrm{red}$ from the finite group of $X$ to $G_0$ such that:

1. $\mathrm{red}$ is a reduction homomorphism: it is reduction of matrices at the chosen places, it is multiplicative and surjective, and its kernel on the level subgroup is the principal congruence subgroup of level $g_0 g_1$;
2. each chosen place $v$ has a split place $s$ over it;
3. for each lift $x$ of $\gamma$ at $s$ over $v \in \mathrm{Pl}_k$, there is $k'$ in the level set of $X$ with $\psi_Y(c x c^{-1}) = \kappa(k')$, $\mathrm{red}(k')_{v} = \gamma$, and $\mathrm{red}(k')_{v'} = 1$ for each other chosen place $v'$.

Here $\kappa(k')$ is the image of $k'$ under the identification of the adelic groups of $X$ and $D$, conjugated by $t$.

**Theorem 3.12.1 (Frame reduction).** Assume that $F$ is the maximal real subfield of $E$ and that $\psi_Y$ is standard. Then a frame reduction exists.

Lean: `GlobalTheory.LabPin.frameRed_exists` (also `GlobalTheory.T.exists_maximalCompact_reduction_standardFrame`, a second name).

*Proof.*

1. Two places of the CM field are equal if their split places are equal. With this fact, there are a conjugator $c$ and local frames at the chosen places such that the lifts act by reductions.
2. There is a reduction $\rho$ that acts on each local frame as the reduction of matrices. The chosen places contain one place in each conjugate pair, so $\rho$ is well defined. Put $\mathrm{red} = \rho$.
3. A matrix acts as a reduced matrix on a frame of a degree one prime if and only if its entries reduce to those of the matrix. This gives the first part of property 1. $\rho$ is multiplicative and surjective, and its kernel is the congruence subgroup of level $g_0 g_1$, since the level of $X$ is $g_0 g_1$.
4. Each chosen place is the place of a split place. This gives property 2.
5. For a lift $x$ of $\gamma$, step 1 gives $k'$ in the level set with the action on the frames. The compact group of $Y_0$ is normal, so $\psi_Y(c x c^{-1})$ conjugated by $t$ lies in the finite adelic part, and its archimedean component is $1$. Step 1 gives $\mathrm{red}(k')_v = \gamma$ and $\mathrm{red}(k')_{v'} = 1$ for $v' \ne v$. $\square$

### Label tuples and their operators

For each row $\sigma$ of $D$ there is a type $\mathrm{ft}(\sigma)$ and, at each chosen place $v$ over $g_k$, a label $\ell_k(\sigma, v)$. The *label tuple* of $\sigma$ is $\ell(\sigma) = (\ell_k(\sigma, v))$. Each label has a series idempotent $e_k(\ell)$ in the group algebra of $\mathrm{GL}_r(\mathbb Z/g_k)$. The *series coefficient* of a tuple $\ell$ at $\gamma \in G_0$ is
$$c_\ell(\gamma) = \prod_{(k, v)} e_k(\ell_{k,v})(\gamma_v).$$
Let $\mathrm{sec}$ be a section of $\mathrm{red}$ with values in the level set. The *tuple operator* of $\ell$ is
$$A_\ell = \sum_{\gamma \in G_0} \overline{c_\ell(\gamma)}\, R(\mathrm{sec}(\gamma)),$$
with $R$ the right regular action on $L^2$ of the quotient of $X$. Let $b_\sigma$ be the row vector of $\sigma$: the image of the $\sigma$-th orthonormal vector under an isometry $\iota$ of the row space of $D$ into $L^2$.

A family of types *has labels* if each label is a label of $D$ and, at each split place over a chosen place, the series idempotent of the label fixes each vector of the type that is fixed by the lifts of $1$. The *label tie* for $\iota$ says three things: each $\ell_k(\sigma, v)$ is a label, each label tuple is good, and $A_{\ell(\sigma)} b_\sigma = b_\sigma$ for each row $\sigma$.

**Theorem 3.12.2 (Label tie from type series).** Assume that $F$ is the maximal real subfield of $E$ and that $\psi_Y$ is standard. Let the realisation data of $D$ give, for each row $\sigma$, an automorphic form $e_\sigma$ on the adelic group of $Y_0$ with these properties:

1. $e_\sigma$ lies in the isotypic part of the conjugate type of $\mathrm{ft}(\sigma)$;
2. $e_\sigma(y\kappa(k)) = e_\sigma(y)$ for each $k$ in the level subgroup of level $g_0 g_1$;
3. $e_\sigma(\gamma y) = e_\sigma(y)$ for each rational point $\gamma$;
4. the row vector $b_\sigma$ is, up to a constant and conjugation, the function $x \mapsto e_\sigma(x t)$ on the quotient of $X$.

If the family of types has labels and all types are good, then the label tie holds for $\iota$.

Lean: `GlobalTheory.LabPinTop.labTie_of_series` (also `GlobalTheory.T.labels_fixed_by_tupleOperator_of_typeSeries`, a second name).

*Proof.*

1. The first two parts of the label tie are the hypotheses on labels and good types.
2. Take a frame reduction $(c, \mathrm{red})$ and a section $\mathrm{sec}$. Each $\kappa(\mathrm{sec}(\gamma))$ lies in the image of $\psi_Y$; choose a preimage $\lambda(\gamma)$.
3. The series idempotents fix the vectors of the type that are fixed by the lifts of $1$. Summed over $\gamma$, this gives the sum of series coefficients under right translation by the lifts $\lambda(\gamma)$.
4. By the fixed vector identity for an isotypic part of a conjugate type, and properties 1 and 2,
$$\sum_{\gamma} \overline{c_{\ell(\sigma)}(\gamma)}\, e_\sigma\bigl(y\,\kappa(\mathrm{sec}(\gamma))\bigr) = e_\sigma(y)$$
for each $y$.
5. Let $\Phi(y) = \overline{a\, e_\sigma(y)}$ with the constant $a$ of property 4. Then $\Phi$ is left invariant under rational points by property 3, and $b_\sigma(x) = \Phi(x t)$ for almost every $x$.
6. Right translation by $\mathrm{sec}(\gamma)$ commutes with this almost everywhere identity. With step 4 this gives $A_{\ell(\sigma)} b_\sigma = b_\sigma$ in $L^2$. $\square$

**Theorem 3.12.3 (Label tie at a realisation).** Assume that $F$ is the maximal real subfield of $E$ and that $\psi_Y$ is standard. Let the realisation data match the level of $X$: each $k$ in the level subgroup has $\kappa(k)$ in the level set of the face, and the face character at $\kappa(k)$ is $\overline{\chi_2(k)}$. Assume that each $e_\sigma$ lies in the isotypic part of $\mathrm{ft}(\sigma)$ inside the multiplicity space of the face, that the family of types has labels and that all types are good. Then the label tie holds for $\iota$.

Lean: `GlobalTheory.LabPinAt.labTie_at` (also `GlobalTheory.T.realisationLabels_normalised_of_rowsTypes_levels`, a second name).

*Proof.*

1. Each element $T$ of the multiplicity space satisfies $T(gk) = \chi(k) T(g)$ for $k$ in the level set and $T(\gamma g) = T(g)$ for rational points $\gamma$. This holds on the generators, and both properties are linear.
2. On the level subgroup of $X$, the level character $\chi_2$ is $1$. With the level match, $\chi(\kappa(k)) = \overline{\chi_2(k)} = 1$. So step 1 gives property 2 of the last theorem, and it gives property 3.
3. The last theorem gives the label tie. $\square$

### The three ties

A *saturated realisation* of $D$ consists of a Hida setting $X$ with a good operator, a selection of spectral data with an isometry $\iota$ of row spaces, and the realisation data with a face. It carries, as fields, the automorphic tie of $X$ and the row dictionary tie for $\iota$, and it matches the level.

**Theorem 3.12.4 (Ties of a saturated realisation).** Assume that $F$ is the maximal real subfield of $E$ and that $\psi_Y$ is standard. Let $s$ be a saturated realisation in which each $e_\sigma$ lies in the isotypic part of $\mathrm{ft}(\sigma)$. If the family of types has labels and all types are good, then the automorphic tie, the row dictionary tie and the label tie hold for $s$.

Lean: `GlobalTheory.Sat.ties_at` (also `GlobalTheory.T.constructedSpectralObjects_irreducibilityConditions`, a second name).

*Proof.* The first two ties are fields of $s$. The label tie at a realisation gives the third. $\square$

**Remark 3.12.5 (Formalization).** The frame reduction is in ExistsMaximalCompactReductionStandardFrame.lean, line 17. `FrameRed` is in SerFixOne.lean, line 101, `LabTie` at line 54, `IsSec` at line 58, `serCoef` at line 60 and `TypeLab` at line 96. `IsRedHom` is in RowLevelMatch.lean, line 27. The label tie from type series is in LabelsFixedByTupleOperatorOfTypeSeries.lean, line 75, with the helpers `kap_mem_GfC` and `R_translate_ae` (lines 18 and 34). The helper file declares `namespace GlobalTheory.LabPinTop` twice in a row: it closes the namespace and opens it again before the main theorem (lines 71 and 73). The label tie at a realisation is in RealisationLabelsNormalisedOfRowsTypesLevels.lean, line 30; it uses `mult_lev_left` (line 13) and `level_subgroup_properties` for the fact $\chi_2 = 1$. The ties of a saturated realisation are in ConstructedSpectralObjectsIrreducibilityConditio.lean, line 10. The module name is cut off: it ends in "Conditio", and so does its statement file. The proof is one anonymous constructor with two field projections, `s.S.autTie` and `s.S.rowTie`. All four statement files (line 8 in each) import the proof modules and give the second names with `first | exact @...`.
