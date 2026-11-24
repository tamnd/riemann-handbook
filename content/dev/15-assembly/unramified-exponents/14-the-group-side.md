---
title: The group side
decls:
  - GlobalTheory.T.exists_nbc_auSide_true_of_isEmpty_loc
  - GlobalTheory.AutQuot.exists_nbc_auSide_auTrue_of_isEmpty
  - GlobalTheory.AutQuot.exists_nbc_auSide_true_of_empty
  - GlobalTheory.HeightCounting.TopA.conclusion_of_cusp_galois_true
  - GlobalTheory.HeightCounting.TopA.conclusion_of_local_parameters_true
  - GlobalTheory.HeightCounting.TopA.conclusion_of_group_side
  - GlobalTheory.HeightCounting.TopA.exists_sideA_alt
  - GlobalTheory.T.types_true_of_ray_class_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The group side

This section proves the theorem behind item 1 of [the stage statements](/entry/all-stages-of-specializations-alt/) of Section 6. For a datum $D$ with no localized places, it gives a layer of $D$ and a host embedding of its character frame at which the automorphic side is realised, the character group condition holds, and the representation parameters hold. The same Galois level statement uses it at every stage with an empty set of localized places. The proof builds the data one at a time on successive modified data: tame generators with a green cuspidal labelling, a Weil-Deligne tie with true labels, a character side, a boundary condition with an automorphic side, the types at the ray primes, and the Weil-Deligne side. At each step the conclusion transfers back to $D$.

We take the following as given. They are fields of $\mathcal{H}_A$ and $\mathcal{H}_E$ in Section 1.

1. Green's classification of the irreducible characters of $\mathrm{GL}_d(\mathbb{F}_q)$, with the cuspidal characters labelled by regular characters of $\mathbb{F}_{q^d}^\times$ ([depth zero representations and types](/learn/representations/#depth-zero-representations-and-types)).
2. [Global Artin reciprocity](/learn/class-field-theory/#global-class-field-theory) and the existence of the ray class field of each modulus.
3. The Chebotarev density theorem in the form: for a finite Galois extension $L/F$ of number fields, an element $g$ of $\mathrm{Gal}(L/F)$ and a finite set $S$ of primes of $F$, there is a prime of $F$ of degree one, outside $S$ and unramified in $L$, whose Frobenius class contains $g$ ([the splitting of primes](/learn/number-fields/#the-splitting-of-primes)).
4. A de Rham representation of the absolute Galois group of a finite extension of $\mathbb{Q}_\ell$ is potentially semistable ([crystalline, de Rham and potentially semistable representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations)).
5. Finiteness of automorphic forms on $\mathrm{GL}_a$ over a CM field: for an open compact level and a finite dimensional representation at infinity, the space of automorphic forms of that type is finite dimensional.

Let $D$ be a datum with host field $E$, a character frame $\mathrm{cf}$ with places $P$ and weights $W$, an embedding $j_E : E \to \overline{\mathbb{Q}}$, and a map $\mathrm{rep}$ from the finite types of $D$ to finite types of rank $r$ over $E$. The host of $D$ has tame primes $g_k$ and integers $Q_S$, $q$ and $d$. Write $K(\overline{\mathbb{Q}})$ for the field of $D$ in $\overline{\mathbb{Q}}$ along $j_E$.

**Definition 6.14.1 (Weil-Deligne ties and sides).** A *Weil-Deligne tie* $T$ for $D$ assigns to each place $w$ a map $T_w$ from local Galois parameters to Weil-Deligne representations. Its labels are *true* if they are the labels of the types at the tame primes, and *conjugate* if they are stable under the conjugation of $E$. A *group side* $\Gamma$ of $D$ gives a root of unity $\zeta_k$ at each tame prime $g_k$. A *row side* $R_s$ gives a local Galois representation $R_s(\sigma, w)$ at each place $w$ and a Satake datum. The *representation parameters* hold for $\mathrm{rep}$ and $R_s$ at $T$ if, for each type $\sigma$ and place $w$, the representation $T_w(R_s(\sigma, w))$ has the parameters of $\mathrm{rep}(\sigma)$ and the Satake data agree.

**Definition 6.14.2 (Automorphic side).** An *automorphic side* $A$ at a tie $T$ gives, for each Galois type $\sigma$, an automorphic class with multiplicity one, spherical at the places of a set, with Satake parameters and weights, unramified at the places outside the level, such that at each such place the Hecke polynomial
$$
\begin{aligned}
X^n + \sum_{k = 1}^{n} (-1)^k N(w)^{k(k-1)/2} c_k X^{n-k}
\end{aligned}
$$
equals the characteristic polynomial of Frobenius of the twist of $\sigma$ by $(1 - n)/2$. The automorphic side is *realised* at $T$ if $T_w$ of the local component of $A$ at $w$ is the local reciprocity of the class of $\sigma$.

**Definition 6.14.3 (Conclusion at a datum).** The *conclusion* at $(D, \mathrm{cf}, j_E, \mathrm{rep})$ says that there are a layer $L$ of $D$ with the conditions on $Z$ and on $\eta$, with layered datum $D_L$, and a host embedding $A$ of the layered character frame along $j_E$, with a tie $T_A$, an automorphic side, a row side and a group side, such that:

1. the character group condition holds at $T_A$, the automorphic side of $A$ is realised at $T_A$, and the representation parameters hold for $\mathrm{rep}$ at $T_A$;
2. the types of $L$ are true at $P$ and $W$;
3. $L$ has the places, the central data, the localization and the data at $\Omega$ of $D$;
4. $\zeta_k$ is the generator of the label datum at $g_k$, and the labels of $T_A$ are conjugate.

**Theorem 6.14.4 (Boundary conditions and automorphic sides).** Let $D$ be a datum whose set of localized places is empty, and let $T$ be a Weil-Deligne tie. Then there are a boundary condition $C$ for the automorphic data of $D$ and an automorphic side $A$ of the datum $D_C$ with boundary $C$ that is realised at $T$.

Lean: `GlobalTheory.AutQuot.exists_nbc_auSide_true_of_empty` (also `GlobalTheory.AutQuot.exists_nbc_auSide_auTrue_of_isEmpty` and `GlobalTheory.T.exists_nbc_auSide_true_of_isEmpty_loc`, second names with the arguments in another order).

*Proof.* The boundary condition $C$ has no local places, and it asks at each place $w$ that the representation is spherical at some place over $w$. The automorphic side takes for each $\sigma$ the automorphic class of $\sigma$: this map is onto, it respects isomorphism, and two isomorphic representations have the same multiplicity. The class is spherical at its places, and its Satake parameters and weights are those of $\sigma$. It is unramified outside the level because its local component is spherical there. A vector fixed by the spherical subgroup gives the Hecke polynomial in the definition. The realisation holds because at each local place the tie sends the local component to the local reciprocity of the class of $\sigma$. $\square$

**Theorem 6.14.5 (Conclusion from a tie and a character side).** Assume statements 2 to 4. Let $D$ have no localized places, assume each $g_k$ is a ray prime of $K(\overline{\mathbb{Q}})$ for the modulus $Q_S q d$, and assume the types of $D$ are true at $P$ and $W$. Let $\Gamma$ be a group side with $\zeta_k$ the generator of the label datum at $g_k$, assume the character condition for $\mathrm{cf}$, let $T$ be a tie with true and conjugate labels, let $R_s$ be a row side with the representation parameters for $\mathrm{rep}$ at $T$, and assume the character group condition at $T$ and a character side. Then the conclusion holds at $(D, \mathrm{cf}, j_E, \mathrm{rep})$.

Lean: `GlobalTheory.HeightCounting.TopA.conclusion_of_cusp_galois_true`.

*Proof.* The theorem on boundary conditions gives $C$ and an automorphic side realised at $T$ on $D_C$. On $D_C$ the places are nonempty. Ray class fields and the Chebotarev theorem give types at the ray primes $g_k$ with the parameters of the place side. These types give a datum with a group side and the types. By statement 4, the Galois representations of the side are potentially semistable, which gives a Weil-Deligne side. The pieces form a layer with a host embedding, and the conclusion holds on the modified datum. Each modification keeps the places, the central data, the localization and the data at $\Omega$, so the conclusion transfers back to $D$. $\square$

**Theorem 6.14.6 (Conclusion from local parameters).** Assume statements 2 to 5. Let $D$, $\mathrm{cf}$, $j_E$, $\mathrm{rep}$, $\Gamma$ and $T$ be as in the previous theorem, with the ray prime, type, $\zeta$ and character conditions, true and conjugate labels for $T$, and a row side $R_s$ with the representation parameters at $T$. Then the conclusion holds.

Lean: `GlobalTheory.HeightCounting.TopA.conclusion_of_local_parameters_true`.

*Proof.* Statement 5 and the true types at the places give a modified datum with the character group condition and a character side. The previous theorem applies on this datum, and the conclusion transfers back to $D$. $\square$

**Theorem 6.14.7 (Conclusion from a group side).** Assume statements 2 to 5. Let $D$ have no localized places, with the ray prime condition and true types, let $\Gamma$ be a group side with $\zeta_k$ the generator of the label datum at $g_k$, assume the character condition, and assume that the rows of $\mathrm{rep}$ have depth. Then the conclusion holds.

Lean: `GlobalTheory.HeightCounting.TopA.conclusion_of_group_side`.

*Proof.* Since the rows have depth, there is a row datum with Weil-Deligne parameters and the representation parameters for $\mathrm{rep}$. This gives a modified datum with a tie $T$ with true and conjugate labels and a row side. We transfer the character condition and the representation parameters to the modified datum, apply the theorem on local parameters, and transfer the conclusion back. $\square$

**Theorem 6.14.8 (Group side at a datum).** Assume statements 1 to 5. Let $h_L$ be a recursion datum and $D$ a datum with no localized places. Let $\mathrm{cf}$, $j_E$ and $\mathrm{rep}$ be as above. Assume that each exponent of $D$ is an integer, that the types of $D$ are true at $P$ and $W$, that the rows of $\mathrm{rep}$ have depth, and that each $g_k$ is a ray prime of $K(\overline{\mathbb{Q}})$ for the modulus $Q_S q d$. Then the conclusion holds at $(D, \mathrm{cf}, j_E, \mathrm{rep})$.

Lean: `GlobalTheory.HeightCounting.TopA.exists_sideA_alt` (also `GlobalTheory.T.types_true_of_ray_class_alt`, a second name).

*Proof.* Green's classification and global Artin reciprocity give tame generators with a green cuspidal labelling: a layer $L$ with the conditions on $Z$ and $\eta$, such that the layered datum has no localized places and true types, agrees with $D$ in its places and other data, and has a group side with $\zeta_k$ the generator of the label datum at $g_k$ and the character condition. The integrality of the exponents is used here. The depth of the rows transfers to the layered datum. The theorem on a group side applies there, and the conclusion transfers back to $D$. $\square$

**Remark 6.14.9 (Formalization).** The theorems are at [ConclOfGrp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L161) (lines 88, 109 and 127; the conclusion `ConclAlt` at line 16), [ConclOfGrpStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrpStatement.lean#L13), [ExistsNbcAuSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsNbcAuSide.lean#L79) (line 101) and [ExistsNbcAuSideStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsNbcAuSideStatement.lean#L15). Statement 5 is not used: it is passed to `exists_cgTrue_charSide`, which drops it (ExistsCgTrueCharSide.lean, line 93, `intro hL _ D hE T cf hP`). Statement 3 is not used either: `ParRay.exists_types` drops it (ExistsTypes.lean, line 23, `intro hray _ D hE jE Pl hg`). In the theorem on boundary conditions, the condition on the embedding of spherical vectors is proved by `isEmptyElim`, so it holds vacuously because the set of localized places is empty. The name "types true of ray class" does not describe the statement, whose hypotheses include true types. The step with tame generators is `exists_tame_generators_green_cuspidal_labelling`, which has no entry here. We did not unfold `Lay0`, `setK`, `CharFrameHostEmbedding`, `CGTrueT`, `CharSide`, `RowDepth`, `ChiTOk`, `LabTrue`, `LabConj`, `NBC` or the transfer equalities, so the definitions above give their roles. The relay runs with `maxHeartbeats 1000000`, and the main theorem with `maxHeartbeats 4000000`.
