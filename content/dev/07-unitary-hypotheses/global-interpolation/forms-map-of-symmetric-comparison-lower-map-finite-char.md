---
id: forms-map-of-symmetric-comparison-lower-map-finite-char
title: The forms map from a symmetric comparison
kind: theorem
decl: GlobalTheory.RedPt0.formsMap_of_symmetricComparison_lowerMap_finiteChar
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.FormsMapOfSymmetricComparisonLowerMapFiniteChar
covers: 439
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion6`, the five facts about the period map on forms that the field `aPt0` of [HypsAlt](/step/hyps-alt-def/) asks for, from symmetric tied forms with three properties. [The forms map at every true column member](/entry/forms-map-at-every-true-column-member/) checks the three properties for true columns and applies it.

## Statement

Let $D$ be a datum (`D7`), $u$ a word and $m$ the top step. The member forms `D.fm u` give:

- $\mathcal F_m$ (`Fi m`), a space of functions on the classes $\mathcal C_m$ at step $m$, with a Hermitian form $\langle \cdot, \cdot \rangle_C$ (`ipC`);
- a finite set $\mathcal C_P$ (`clsP`), a map $t \colon \mathcal C_P \to \mathcal C_m$ (`til`), and for each $c$ an injective homomorphism $s_c$ from a finite group to the stabilizer of $t(c)$ (`stabMap`);
- the period map $\mathrm{Pt} = \mathrm{lowerMap} \circ \mathrm{ev}_z$ from forms to a space $W$ with a Hermitian form $\langle \cdot, \cdot \rangle_P$ (`ipP`) and a subspace $W_C$ (`ptC`);
- Hermitian lattices $\Lambda$ (`lat m`) and $\Lambda_P$ (`ptLat`) over the number field $\mathbf L$ = `D.what₂.LL`, with embeddings onto $\mathcal F_m$ and $W_C$;
- the constant $b = \prod_\tau T^{-\deg \tau} \beta(\tau)^2$ (`ptB`), where $\beta(\tau)$ is `beOn τ`.

`Conclusion6 D u` is the conjunction of:

1. $t$ is injective;
2. each $s_c$ is bijective;
3. $\mathrm{Pt}(\mathcal F_m) \subseteq W_C$;
4. $\mathrm{Pt}$ is defined over $\mathbf L$ (`PRat`), so it gives an $\mathbf L$-linear map $\mathrm{Pt}_{\mathbf L}$ between the spaces of the lattices; $\mathrm{Pt}_{\mathbf L}(\Lambda) \subseteq \Lambda_P$; and at each infinite place $v$ of $\mathbf L$, the majorant of $\mathrm{Pt}_{\mathbf L} x$ is at most $b$ times the majorant of $x$;
5. $\operatorname{Re} \langle \mathrm{Pt}\,\varphi, \mathrm{Pt}\,\varphi \rangle_P \le b \operatorname{Re} \langle \varphi, \varphi \rangle_C$ for $\varphi \in \mathcal F_m$.

**Theorem.** Let $T_f$ be symmetric tied forms for $D$ and $u$ (a structure `FormsTiedSym D u Ch chOf`). Assume:

- `LowerMapTieS T_f`: in the coordinates of $T_f$, the lower map acts by the branching tensor `brTen D u`;
- `BeOnTie D u`: each $\beta(\tau)$ is the operator norm of the branching map `brOne` from the weight $\lambda_\tau$ to the weight $\sigma_\tau$;
- the level character $\chi$ of $T_f$ at step $m$ has finite order and takes values in the image of $\mathbf L$.

Then `Conclusion6 D u` holds.

## Proof

1. **A pending object.** `exists_integralPendingObject_symmetricFormsLevel` builds a `Pend D u` $P$: maps $\mathrm{br}_\tau$ with norm $\beta(\tau)$, and coordinates at each finite place in which $\mathrm{Pt}$ is block diagonal with blocks $\mathrm{br}_\tau$ and lattice vectors are integral. `ArchimedeanSignatureMatching P` says that each $\mathrm{br}_\tau$ is a branching map (`IsBr`): equivariant for $\mathrm{GL}_{N-1}(\mathbb C)$, not zero, integral, with bounded Fock norm. Integrality uses the finite order of $\chi$: its values are roots of unity in $\mathbf L$.
2. **Clauses 1 to 3.** `symmetric_level_clauses_hold` gives them, with the bound at infinite places.
3. **Assembly.** `classMap_estimate_of_partial` proves clause 4 from $P$, prime by prime, and clause 5 from the bound at the infinite place of $\mathbf L$.

## In the Lean code

The theorem is in [FormsMapOfSymmetricComparisonLowerMapFiniteChar.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FormsMapOfSymmetricComparisonLowerMapFiniteChar.lean#L12). `Conclusion6` and `Pend` are in [ProductFirstZerothParts.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/ProductFirstZerothParts.lean#L334); the three lemmas are in [ExistsIntegralPendingObjectSymmetricFormsLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsIntegralPendingObjectSymmetricFormsLevel.lean#L291), [SymmetricLevelClausesHold.lean](lean:Formalism/LocalToGlobal/GlobalTheory/BlockActions/SymmetricLevelClausesHold.lean#L6) and [FiniteModelOfAdmissibleTransports.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/FiniteModelOfAdmissibleTransports.lean#L2259).

We have not read the proofs of the four lemmas behind step 2. Clauses 1 and 2 do not use the two tie hypotheses, only the existence of $T_f$.

The name `ArchimedeanSignatureMatching` is misleading: the predicate (`IsBr` for each $\mathrm{br}_\tau$) involves no signature and no archimedean place.
