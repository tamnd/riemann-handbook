---
title: The fourth clause and Part I
decls:
  - GlobalTheory.T.arcFamily_fourthCondition_invertible_pushforward
  - GlobalTheory.LN.ArcClause.arc_clause
  - GlobalTheory.T.modelSystems_jointProperties_of_laws
  - GlobalTheory.LN.partI_of_inputs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The fourth clause and Part I

The construction of the projective models of PEL moduli spaces is stated as a list of clauses. The fourth clause says that each arc $a$ over an arc base $(O', \varpi)$ is the degeneration of a unique map $\operatorname{Spec} O'[[X]] \to Y$, and that this map specialises at $X = \varpi$ to every point over $O'$ with the arc data of $a$ at $\varpi$. In this section we derive the fourth clause from [the arc family statement](/entry/arc-fam/) and a list of results on models, and then we derive Part I of the construction, which collects the first clauses for a whole system of models. Part I is used in the proof of [the semistable reduction of the arc family](/entry/part-i-of-semistable-reduction-of-arc-fam/). For the background see [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) and [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications) in Volume 1.

### The clauses

We keep the notation of the earlier sections. In particular $Y$ is a model of $X_o$ over the valuation ring $V$ of $F$, with semi-abelian scheme $G$, line bundle $L$, open immersion $j : X_{o,F} \to Y$ and abelian locus $Y^{\mathrm{ab}}$. Arc data at a trait are defined in [the section on frames](/entry/exists-is-frame-pow-sq/); the same definition makes sense over any local domain $R$ with an ideal $I$, a map $O' \to R$ and an element $u \in R$.

**Definition 6.7.1 (Fourth clause).** The model $Y$ satisfies the *fourth clause* if, for every arc base $(O', \varpi)$ with $O'$ of characteristic $0$, every $b : V \to O'$ and every arc $a$ over $(O', b)$, there is a map $\chi : \operatorname{Spec} O'[[X]] \to Y$ with these properties.

1. A map $\chi'$ equals $\chi$ if and only if: $\chi'$ lies over $b$; a point $x$ of $\operatorname{Spec} O'[[X]]$ maps to $Y^{\mathrm{ab}}$ exactly when $X \notin x$; each point $x$ with $\varpi X \notin x$ maps into the image of $j$; and $\chi'$ has the arc data of $a$ for the ideal $(X)$, the constants $O' \to O'[[X]]$ and the parameter $X$.
2. If $\varpi$ is irreducible, then every point $y' : \operatorname{Spec} O' \to Y$ over $b$ whose generic point lies in the image of $j$ and which has the arc data of $a$ for $(\varpi)$ with parameter $\varpi$ is $\chi \circ \operatorname{ev}$, where $\operatorname{ev} : O'[[X]] \to O'$ is the evaluation $X \mapsto \varpi$ over $O'$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Model.N4`.

**Definition 6.7.2 (Ample frames).** The model $Y$ has *ample frames* if there are an odd $m$ that is a unit in $V$, a finite surjective map $\pi : Z \to Y$, a semi-abelian scheme $t$ over $Z$ with a map to $G$ over $\pi$, and a system of charts of $t$ with frames of level $m^2$ that make $L^{m^2}$ relatively very ample.

Lean: `GlobalTheory.LN.Amp`.

The model satisfies the *level structure conditions* at a prime $p$ if the action of the level group and the descent hold, the pushforward of $L$ to $Y$ is an invertible sheaf (we say $L$ has *invertible pushforward*), the level points of order prime to $p$ extend over the abelian locus, and good reduction extends over complete discrete valuation rings and over the unit balls of complete fields in which $|p| < 1$.

**Definition 6.7.3 (Part I).** *Part I* is the statement: Siegel families of level $n^j \geq 3$ exist for every odd prime $n \neq p$, and for every PEL datum $D$ with $p + q \geq 1$ and every family of moduli spaces $X_o$, there is a system of models $Y_{p, W}$, one for each prime $p$ and each valuation ring $W$ of $\mathbb{C}$ with $|p|_W < 1$, such that each system satisfies the transition clause, every model in it has split fibres and satisfies the third and fourth clauses, and the global models dominate the local ones.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.PartI`.

### Inputs

We use these results of the Lean development, each proved outside this chapter.

**Theorem 6.7.4 (Descent of the generic point).** If $(g, y_1)$ has trait data for $a$, with $g : O'[[X]] \to R_1$ finite and $R_1$ integrally closed, then $y_1$ comes from a point $y$ over $\operatorname{Frac} O'[[X]]$, and $(\mathrm{id}, y)$ has trait data for $a$.

Lean: `GlobalTheory.T.arcGenericPoint_descends_to_powerSeries`.

**Theorem 6.7.5 (Extension over the power series ring).** If $Y$ has ample frames and $y$ comes from an arc point with frames of level $1$ and $m^2$, then $j \circ y$ extends to a map $\chi : \operatorname{Spec} O'[[X]] \to Y$.

Lean: `GlobalTheory.T.arc_generic_point_extends_powerSeries`.

**Theorem 6.7.6 (The extension has the right loci).** If $\chi$ extends $j \circ y$ and $(\mathrm{id}, y)$ has trait data for $a$, then $\chi$ lies over $b$, maps $x$ to $Y^{\mathrm{ab}}$ exactly when $X \notin x$, and maps each $x$ with $\varpi X \notin x$ into the image of $j$.

Lean: `GlobalTheory.T.arc_abelianLocus_and_moduli_of_traitData`.

**Theorem 6.7.7 (Arc data along $X$).** If $L$ has invertible pushforward, $\chi$ extends $j \circ y$ and $(\mathrm{id}, y)$ has trait data for $a$, then $\chi$ has the arc data of $a$ for $(X)$ with parameter $X$.

Lean: `GlobalTheory.T.extendedArc_uAdicUniformisation_of_arcData`.

**Theorem 6.7.8 (Uniqueness).** Let $R$ be an admissible local base with a proper ideal $I$ and an injective map $f : O' \to R$. Two maps $\operatorname{Spec} R \to Y$ over $b$ whose generic points lie in the image of $j$ and which both have the arc data of $a$ for $(I, f, u)$ are equal.

Lean: `GlobalTheory.T.model_points_eq_of_same_degeneration_data`.

**Theorem 6.7.9 (Specialisation at the uniformiser).** If $O'$ is a complete discrete valuation ring with uniformiser $\varpi$, $\operatorname{ev}$ is the evaluation at $\varpi$, and $\chi$ has the arc data of $a$ for $(X)$ with parameter $X$, then $\chi \circ \operatorname{ev}$ has the arc data of $a$ for $(\varpi)$ with parameter $\varpi$.

Lean: `GlobalTheory.T.arcData_specialise_at_uniformiser`.

**Theorem 6.7.10 (Third clause).** A model that satisfies the level structure conditions at $p$ satisfies the third clause.

Lean: `GlobalTheory.T.model_uniformisation_of_abelianLocus_directImage`.

### The fourth clause

**Theorem 6.7.11 (Fourth clause).** Assume the inputs of the models and the arc family statement. Let $Y$ be a model of $X_o$ that satisfies the level structure conditions at a prime $p$ and has ample frames. Then $Y$ satisfies the fourth clause.

Lean: `GlobalTheory.T.arcFamily_fourthCondition_invertible_pushforward` (also `GlobalTheory.LN.ArcClause.arc_clause`, a second name).

*Proof.* Fix $(O', \varpi)$, $b$ and $a$. Let $m$, $Z$, $\pi$ and $t$ be the data of the ample frames. Since $m$ is a unit in $V$, its image is a unit in $O'$. The arc family statement gives $R_1$, $g$ and $y_1$ with trait data and frames of level $1$ and $m^2$. By the descent of the generic point, $y_1$ comes from a point $y$ over $\operatorname{Frac} O'[[X]]$ with trait data, and by the extension over the power series ring, $j \circ y$ extends to $\chi : \operatorname{Spec} O'[[X]] \to Y$. By the two results on the extension, $\chi$ lies over $b$, has the right loci, and has the arc data of $a$ along $X$. The second result uses that $L$ has invertible pushforward.

*Part 1.* We have shown that $\chi$ has the four properties. Conversely, let $\chi'$ have them. Since $O'$ is local and principal, $O'[[X]]$ is a local domain of characteristic $0$, complete for $(X)$, so it is an admissible base for the proper ideal $(X)$. The element $\varpi X$ is nonzero, so it is not in the generic point, and the generic point of $\chi'$ lies in the image of $j$. So $\chi'$ comes from a point $y'$ over $\operatorname{Frac} O'[[X]]$. Both $\chi$ and $\chi'$ have the arc data of $a$ for $(X)$, so $\chi' = \chi$ by uniqueness.

*Part 2.* Assume that $\varpi$ is irreducible. Then $(O', \varpi)$ is not the field case, since $1$ is a unit, so $O'$ is a complete discrete valuation ring with maximal ideal $(\varpi)$. Let $y'$ and $\operatorname{ev}$ be as in the clause. Since $\operatorname{ev}(\varpi X) = \varpi^2 \neq 0$, the generic point of $\chi \circ \operatorname{ev}$ lies in the image of $j$. By specialisation at the uniformiser, $\chi \circ \operatorname{ev}$ has the arc data of $a$ for $(\varpi)$ with parameter $\varpi$. Both maps lie over $b$, so uniqueness over $O'$ gives $\chi \circ \operatorname{ev} = y'$. $\square$

### Part I

**Theorem 6.7.12 (Part I).** Assume the inputs of the models, the arc family statement, the statement on systems of models, and the existence of Siegel families. Then Part I holds.

Lean: `GlobalTheory.T.modelSystems_jointProperties_of_laws` (also `GlobalTheory.LN.partI_of_inputs`, a second name).

*Proof.* The existence of Siegel families is the first part of Part I. Fix $D$ with $p + q \geq 1$ and $X_o$. The statement on systems of models gives a system $Y_{p, W}$ that satisfies the transition clause, has global models that dominate the local ones, and in which every model has split fibres and ample frames. The transition clause includes the level structure conditions at $p$ for every model. So each model satisfies the third clause, by the theorem on the third clause, and the fourth clause, by the theorem on the fourth clause. $\square$

**Remark 6.7.13 (Formalization).** The fourth clause is proved in [ArcFamilyFourthConditionInvertiblePushforward.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ArcFamilyFourthConditionInvertiblePushforward.lean#L79), and Part I in [ModelSystemsJointPropertiesOfLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ModelSystemsJointPropertiesOfLaws.lean#L24). The inputs of the models are a twisted base change statement, six bundles of laws, the EGA statements, a uniformisation statement, a PEL statement and the extension of homomorphisms. Of the level structure conditions, only the invertible pushforward is used in the fourth clause (line 95). In Part I the ample frames are used only to get the fourth clause; Part I itself does not keep them. The lift of a point whose image lies in the image of $j$ is the local lemma `exists_lift` (line 33). We did not unfold `Model.HasArcData`, `AmpFrames`, `N2`, `N6` or the inputs listed above.
