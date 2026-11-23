---
title: Part I from semistable reduction
decls:
  - GlobalTheory.arcFam_closed
  - GlobalTheory.partI_of_semistableReduction_of_arcFam
  - GlobalTheory.partI_of_semistableReduction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Part I from semistable reduction

This section assembles the results of the chapter into one statement, *Part I*: Siegel families of large level exist at every prime, and the PEL moduli spaces have systems of local models over the valuation rings above every prime that satisfy the conditions of [the previous section](/entry/exists-local-systems-ample/), together with two more: a uniformization of the semi-abelian scheme at complete local rings, in the sense of [Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction), and arcs over power series rings that realize given degeneration data. Part I is the form in which the proof step [every character of the literature](/step/every-character-of-literature/) uses the moduli spaces. We show that it follows from the semistable reduction theorem.

Fix a CM field $E$ with a host, a PEL datum $D$, moduli spaces $X_l$ for all levels, and a model $Y$ of $X_l$ over $O$ with semi-abelian scheme $G$, as in [the previous section](/entry/models-st-of-semistable-reduction/).

**Definition 5.7.1 (Siegel families of large level).** *Condition N0* is: for all $h \ge 1$, every prime $p$ and every odd prime $n \ne p$, there is $j$ with $n^j \ge 3$ such that a [Siegel family](/entry/top-amp-exists/) of genus $h$ at $p$ and level $n^j$ exists.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.N0`.

Let $R$ be a local domain with maximal ideal $I$ and $G_R$ a semi-abelian scheme with $\mathcal{O}_E$-action over $R$. A *PEL uniformization* of $G_R$ consists of degeneration data over $(R, I)$ with an $\mathcal{O}_E$-action on its character group, a polarized abelian variety $A$ with $\mathcal{O}_E$-action over the fraction field of $R$, and a uniformization of $A$ by the data with the given line bundle on $G_R$, which is $\mathcal{O}_E$-linear and satisfies the trace form condition for $w_0$. It is a *uniformization with torsion* if the values of $\psi$ are units on a given set $U$ and, over every algebraically closed field $F$ over the fraction field and for every $k \ge 1$, the $k$-division points of the data map bijectively, up to equivalence, onto the $k$-torsion of $A(F)$, compatibly with addition, the $\mathcal{O}_E$-action and the Weil pairing.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.PELUnif`, `PELUnif.TorsionIso`, `UniformisationConclusion`.

**Definition 5.7.2 (Uniformization at complete local rings).** A model $Y$ satisfies *condition N3* if for every complete noetherian, integrally closed local domain $R$ of characteristic $0$, every map $\xi : \operatorname{Spec} R \to Y$ that meets the abelian locus, and every semi-abelian scheme $G_R$ with a map to $G$ over $\xi$ whose special fibre is a split extension of an abelian variety by a split torus, $G_R$ has a uniformization with torsion, with $\psi$ a unit on $\xi^{-1}$ of the abelian locus.

Lean: `Model.N3`.

**Definition 5.7.3 (Arc data).** Let $O'$ be a domain of characteristic $0$ with $b : O \to O'$. *Arc input* over $O'$ is a degeneration datum $D_0$ over $O'$ with $\mathcal{O}_E$-action on a nonzero character group $X$, with $\psi$ even, $\tau$ bimultiplicative and $\psi$ a unit everywhere, satisfying the trace form condition for $w_0$, together with a positive definite symmetric form $B$ on $X$, adjoint for the conjugation and divisible by $2M'$, and with division points $\eta$ of order $M$ and $\eta_A$ of order $A$ indexed by $\Lambda$, such that at every geometric point the Lie algebra has the multiplicities of $D$ (counted with the rank of $X$) and there is a Tate isomorphism of division points that carries $\eta$ and $\eta_A$ to the levels.

A map $\chi : \operatorname{Spec} R \to Y$ with an ideal $I \subseteq R$, $f : O' \to R$ and $u \in R$ *has the arc data* of the input if the pullback of $G$ along $\chi$ has a PEL uniformization over $(R, I)$ whose datum is the pullback of $D_0$ along $f$, with matching line bundle, rigidification, action and characters, whose $\psi$ is that of $D_0$ times $u^{B(y,y)/2}$, and whose division points twisted by powers of $u$ map to the points $\eta$ and $\eta_A$ of the universal object.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.ArcIn`, `TateIsoQ`, `GenRel`, `Model.HasArcData`.

**Definition 5.7.4 (Arcs).** Let $O'$ be either a field with $\varpi = 1$, or a complete [[discrete valuation ring|MGM3CNJW9V]] with uniformizer $\varpi$; we call $(O', \varpi)$ an *arc base*. A model $Y$ satisfies *condition N4* if for every arc base and every arc input over $O'$ there is exactly one map $\chi : \operatorname{Spec} O'[[X]] \to Y$ over $b$ that sends exactly the points with $X$ invertible to the abelian locus, sends the points with $\varpi X$ invertible into the image of $j$, and has the arc data with $I = (X)$, $f$ the constant map and $u = X$. Also, when $\varpi$ is a uniformizer, every $O'$-point of $Y$ with the arc data for $(\varpi)$ and $u = \varpi$ is $\chi$ evaluated at $X = \varpi$.

Lean: `Model.N4`, `GlobalTheory.LN.ArcBase`.

**Definition 5.7.5 (Part I).** *Part I* is the statement: condition N0 holds, and for every CM field $E$ with a host, every PEL datum $D$ with $p_D + q_D \ge 1$ and all moduli spaces $X_l$, there is a family of local systems $Y^{p,W}$ such that each satisfies N2, each model in each has split fibres and satisfies N3 and N4, and the family satisfies N6.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.PartI`.

So Part I is the statement that local model systems exist with N3 and N4 in place of ampleness on a cover. To pass from one to the other we use arcs with frames. For a domain $R_1$ and a point $y : \operatorname{Spec} \operatorname{Frac} R_1 \to Y$, sections $b_1, \dots, b_n$ of $L^N$ over $G_y$ form a *frame* if for every complete discrete valuation ring $W$ with a map $R_1 \to W$ and every extension $\chi : \operatorname{Spec} W \to Y$ of $y$, there is a basis of the sections of $L^N$ along $\chi$ that restricts to the $b_i$ at the generic point.

Lean: `GlobalTheory.LN.IsFrame`.

**Definition 5.7.6 (Arc families with frames).** The statement *arc families with frames exist* is: for every model $Y$ of $X_l$ over a valuation ring $V_{W_0}$, every arc base $(O', \varpi)$ with $O'$ of characteristic $0$ over $V_{W_0}$, every arc input over $O'$ and every odd $m$ that is a unit in $O'$, there are an integrally closed domain $R_1$, finite over $O'[[X]]$ with $O'[[X]] \to R_1$ injective, and a point $y_1 : \operatorname{Spec} \operatorname{Frac} R_1 \to X_{l,F}$ such that:

1. $y_1$ lies over $b$ through $O'[[X]]$, and for every complete discrete valuation ring $W$ and every extension $\chi : \operatorname{Spec} W \to Y$ of $y_1$ along $R_1 \to W$, $\chi$ lands in the abelian locus when the image of $X$ is a unit, and otherwise, after a finite extension $W'$, it has the arc data for the maximal ideal of $W'$ with $u$ the image of $X$;
2. there is a frame of $L$ at $y_1$ with one section;
3. there is a frame of $L^{m^2}$ at $y_1$.

Lean: `GlobalTheory.LN.ArcFamSt`, `GlobalTheory.LN.TraitData`.

**Theorem 5.7.7 (Arc families with frames exist).** Arc families with frames exist.

Lean: `GlobalTheory.arcFam_closed`.

*Proof.* This is [the theorem on arc family points with frames](/entry/exists-arc-family-point-with-frames-of-laws/), proved in another chapter from: the expansions of theta functions over complete discrete valuation rings, the sixth law of abelian schemes, the uniformization of triples over complete discrete valuation rings with torsion, the homomorphism extension theorem, the facts that a theta point determines its object and that endomorphisms are determined on torsion, and the uniformization theorem. All of these are results of other chapters, so the statement holds outright. $\square$

**Theorem 5.7.8 (Part I from semistable reduction and arcs).** The semistable reduction theorem and the existence of arc families with frames imply Part I.

Lean: `GlobalTheory.partI_of_semistableReduction_of_arcFam`.

*Proof.* By [the theorem on joint properties of model systems](/entry/model-systems-joint-properties-of-laws/), Part I follows from: base change of twisted principal polarizations, the six sets of laws of abelian schemes, the facts from EGA it uses, the uniformization over discrete valuation rings, the uniformization of linear triples with torsion, the homomorphism extension theorem, the existence of arc families with frames, the existence of local model systems, and condition N0. The inputs other than the last three are results of other chapters. Arc families with frames are the second assumption. Local model systems exist by [the corollary of the previous section](/entry/models-st-of-semistable-reduction/), from the semistable reduction theorem. Condition N0 is the existence of Siegel families of large level, proved in another chapter. $\square$

**Corollary 5.7.9 (Part I).** The semistable reduction theorem implies Part I.

Lean: `GlobalTheory.partI_of_semistableReduction`.

*Proof.* Apply [the previous theorem](/entry/part-i-of-semistable-reduction-of-arc-fam/) with [the existence of arc families with frames](/entry/arc-fam-closed/). $\square$

The semistable reduction theorem itself is proved in [its own chapter](/entry/semistable-reduction-st/), so Part I holds without hypotheses; this is how [every character of the literature](/step/every-character-of-literature/) uses it.

**Remark 5.7.10 (Formalization).** The arc families are filled by `T.exists_arc_family_point_with_frames_of_laws`, with hypotheses `HV`, `Laws6`, `UDvrSt`, `HomExtSt`, `ThetaPtDeterminesSt`, `EndDeterminedOnTorsionSt` and `ThetaUnifAV`, given by `lawsAndExpansions`, `allSixLaws.2.2.2.2.2`, `T.uniformisation_triples_complete_DVR_torsion`, `T.homExtension_semiAbelian_discreteValuationRing`, the two parts of `T.thetaPoint_determines_and_end_determined_torsion` and `thetaUnifAV_closed`. Only the sixth component of `allSixLaws` is used there ([ExistsArcFamilyPointWithFramesProof.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsArcFamilyPointWithFramesProof.lean#L21)). Part I is filled by `T.modelSystems_jointProperties_of_laws`, with the hypotheses `DVR.TwistBaseChangeStatement`, `Laws` to `Laws6`, `Ega`, `USt`, `PelSt`, `HomExtSt`, `ArcFamSt`, `ModelsSt` and `N0`; the last is filled by `T.siegelFamilies_exist`. We did not open the proof of `modelSystems_jointProperties_of_laws`. The semistable reduction theorem `Published.SemistableReductionSt` is used twice in this section, once directly and once through `modelsSt_of_semistableReduction`, and its polarization hypothesis is not used in its conclusion ([SemistableReductionSt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SemistableReduction₂/SemistableReductionSt.lean#L15)).
