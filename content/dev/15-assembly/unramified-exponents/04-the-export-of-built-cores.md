---
title: The export of built cores
decls:
  - GlobalTheory.T.automorphy_of_hypotheses_alt_alt
  - GlobalTheory.Mem.Top.ExportTrue.exportF_prmR_alt_alt
  - GlobalTheory.ExportFirst.exportF_isBuiltE_alt_alt
  - GlobalTheory.T.series_realization_of_published_alt
  - GlobalTheory.ExportClose0.exportAt_bundles_alt
  - GlobalTheory.T.realization_of_published_alt
  - GlobalTheory.ExportClose.exportAt_of_bundles_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The export of built cores

This section proves the export condition for the slot $Q_s$ of built cores, where $s = s(N)$ is the scale of the parameter set of a norm choice extension $N$. Step 1 of [the pair theorem](/entry/exists-base-lattice-of-pair-alt/) of Section 2 uses it, and passes it to the closing theorem of membership. The export condition is global: for all large contexts, every built core must export. The proof reduces it in two moves. First, a built core carries a twisted real join, and the export at the core is a local statement at one datum. Second, the local statement asks for integers and bases of theta series with good twists, and these come from the inputs of Section 5 and from the twist theorem for all powers, which a later chapter proves.

Let $D$ be a datum with base field $F$ and with two primes $g_0, g_1$. A *norm choice* $n$ for $D$ assigns a twist index $i(w)$ to each twisted place $w$, that is, each place where the local twist $\mu_w$ differs from the base twist $\mu_0$. Let $x$ be theta data for $D$, with Hecke form data $E(x)$. Write $\ell_i$ for the prime of a twist index $i$.

**Definition 6.4.1 (Local export).** The datum $(D, n, x)$ *exports* if there are a function $N_0$ from twist indices to $\mathbb{N}$ and finite sets $S_{i,j,b}$, for $j \in \mathbb{N}$ and $b \in \{0, 1\}$, such that:

1. for each twist index $i$ with a nonzero index place, the following holds: if the set hypothesis holds at $i$, then for each $\varepsilon' > 0$, if the sets $\Sigma_{i,j,b}$ of theta series have full rank for $1 \le j \le m$, then for each family of bases of them and each finite set $A$ of finite places of $F$, there are a finite set $Q$ of places, an integer $k'$ and a homomorphism $\psi'$ from the ray class group of $i$ and $Q$ to the units of the ring of level $k'$ at $i$, such that $\psi'^a$ is a good twist for each integer $a$ prime to $\ell_i$;
2. for each twisted place $w$, the set hypothesis holds at $i(w)$, and for $1 \le j \le m$ and each $b$, $\Sigma_{i(w),j,b}$ has full rank and $S_{i(w),j,b}$ is a basis of it.

The set hypothesis is a conjunction of seven conditions, among them $r \ge 100$ and $g_k \ge 2r$ for each $k$.

**Definition 6.4.2 (Export condition).** Let $Q$ be a slot of cores. The *export condition* for $Q$ holds if, for all large contexts, at each base $B$ with frame $f$ where $\mathrm{KP}_x(B, f)$ holds and each untwisted twist datum $T$, every core $c$ in $Q$ at the stage of $B$ exports, with its norm choice and its theta data.

**Definition 6.4.3 (Real, series and Galois sides).** For a datum $D$, a *real side* $X$ consists of the archimedean data of $D$; a *series side* $Y$ over $X$ for Hecke form data $E$ consists of theta series of $X$ with Fourier expansions for $E$; a *Galois side* $G$ consists of a Galois representation with a label. The *field conditions* on $X$ say, among other things, that the field $L_0$ of $D$ is Galois over $\mathbb{Q}$ and contains every $z \in \mathbb{C}$ with $z^{g_k (g_k - 1)} = 1$ for $k = 0, 1$. A *twisted real join* at a point is a real side $X$, a series side $Y$ over $X$, a Galois side $G$, the field conditions on $X$, a cohomology witness, and the base tuple condition at the twist index of each twisted place when the twist datum is untwisted.

We write $\mathcal{H}_{22}$ for the following twenty-two statements from the literature: twelve on Galois cohomology (Chebotarev density, Poitou-Tate duality for totally complex fields, cohomological dimension two, tame local theory, local and global finiteness, local Tate duality, local and global Euler characteristics, unramified orthogonality, archimedean signature matching, the Greenberg-Wiles formula); then Artin reciprocity for ray characters, rapid decay of cusp forms, Chebotarev for primes of degree one, global Artin reciprocity, a toric denominator bound, rationality and integrality of theta series, integrality, transformation and reading ties of Hecke operators. With four statements on Galois representations (finiteness for $\mathrm{GL}$, cuspidal Galois representations, potential semistability of de Rham representations, a character statement) and the conclusion of step 5 for each datum, they make the twenty-seven statements $\mathcal{H}_{27}$. These are the statements of $\mathcal{H}_E$ in Section 1 that enter here.

**Theorem 6.4.4 (Local export).** Assume the first seventeen statements of $\mathcal{H}_{22}$. Let $D$, $n$, $x$ be as above, $X$ a real side, $Y$ a series side over $X$ for $E(x)$ and $G$ a Galois side. Assume:

1. the rationality rows at each nonzero index place, the coefficient bound, and the preservation of the sup lattice by Hecke operators at each $j$;
2. the Hodge condition for $D$ and $G$, and the conclusion of step 5 for $D$;
3. $L_0$ is Galois over $\mathbb{Q}$ and contains every $z$ with $z^{g_k(g_k - 1)} = 1$ for $k = 0, 1$;
4. $n$ is tied to the twist data of $D$, and the base tuple condition for $Y$ holds at the twist index of each twisted place.

Then $(D, n, x)$ exports.

Lean: `GlobalTheory.ExportClose.exportAt_of_bundles_alt` (also `GlobalTheory.T.realization_of_published_alt`, a second name).

*Proof.* There are five steps.

1. [The inputs at a datum](/entry/exists-inputs-of-gal-hodge-n-roots/) of Section 5 give $N_0$ and a record of twenty-one facts on $D$ and $E(x)$. They use Chebotarev for primes of degree one, global Artin reciprocity, the toric bound, the rows, the bounds, the Hodge condition and the roots of unity in $L_0$.
2. For each twisted place $w$, the index $i(w)$ has a nonzero index place. This follows from the tie of $n$ and from $L_0$ being Galois.
3. When $i$ has a nonzero index place and $1 \le j \le m$, let $S_{i,j,b}$ be a basis of averaged series given by the class sums, which exists by one fact of the record. Otherwise let $S_{i,j,b} = \emptyset$.
4. Clause 1 is [the twist theorem for all powers](/entry/twist-all-powers-of-galois-cohomology-class-field/), with the thirteen statements from Chebotarev to Artin reciprocity for ray characters, the conclusion of step 5 and twenty facts of the record.
5. In clause 2 the set hypothesis is a fact of the record, at the index of step 2. The full rank follows from the rationality of the scalars of the theta series, with rapid decay, the base tuple condition and the rows. The basis property is the choice of step 3.

This proves the theorem. $\square$

**Theorem 6.4.5 (Local export from the field conditions).** Assume $\mathcal{H}_{22}$. Let $D$, $n$, $x$, $X$, $Y$ and $G$ be as above. Assume the field conditions on $X$, the Hodge condition for $D$ and $G$, the conclusion of step 5 for $D$, the tie of $n$, and the base tuple condition for $Y$ at the twist index of each twisted place. Then $(D, n, x)$ exports.

Lean: `GlobalTheory.ExportClose0.exportAt_bundles_alt` (also `GlobalTheory.T.series_realization_of_published_alt`, a second name).

*Proof.* We supply hypotheses 1 and 3 of the local export theorem. The rationality rows and the coefficient bound follow from rapid decay, global Artin reciprocity, rationality and integrality of theta series and the field conditions. Hecke operators preserve the sup lattice at each $j$ by rapid decay and the three statements on Hecke operators. The Galois property of $L_0$ and its roots of unity are two of the field conditions. The other hypotheses pass on unchanged. $\square$

**Theorem 6.4.6 (Export at built cores).** Assume $\mathcal{H}_{27}$. Let $h_L$ be a recursion datum and $p$ a parameter set over $h_L$ with scale $s$. Assume that, for all large contexts, at each base $B$ with frame $f$ where $\mathrm{KP}_x(B, f)$ holds and each untwisted $T$, each point with a datum of $p$, a datum of its position and a pinned column has a twisted real join. Then the export condition holds for $Q_s$.

Lean: `GlobalTheory.ExportFirst.exportF_isBuiltE_alt_alt`.

*Proof.* The quantifier over large contexts is kept. Fix a core $c$ in $Q_s$. Since $Q_s$ is the position of the built cores, $c$ comes from a column point $(w, Z, c')$ with a built record $b$, and we may replace $c$ by $c'$. The fields of $b$ give the data of $p$, of its position and the pinned column, so the hypothesis gives a twisted real join $(X, Y, G)$. The Hodge condition for $D$ and $G$ follows from $h_L$, four statements on Galois representations, the cohomology witness and the label of $G$. Now the local export from the field conditions applies, with the field conditions of the join, the conclusion of step 5, the tie of the norm choice of $c'$ and the base tuples of the join. $\square$

**Theorem 6.4.7 (Export at the parameters of an extension).** Assume $\mathcal{H}_{27}$, the published inputs of the third layer and the series input. Let $h_L$ be a recursion datum, and assume the membership statement at layer points for $h_L$ and for the predicate that each row side with the same local row as the point is a good cusp parameter. Let $N$ be a norm choice extension, $S$ an $S$-extension and $\Gamma$ a geometry. Assume that each datum of $N$ at a point gives a datum of the extension with law at that point. Then the export condition holds for $Q_s$, where $s$ is the scale of the parameter set of $(N, S, \Gamma)$.

Lean: `GlobalTheory.Mem.Top.ExportTrue.exportF_prmR_alt_alt` (also `GlobalTheory.T.automorphy_of_hypotheses_alt_alt`, a second name).

*Proof.* By the theorem on export at built cores, it is enough to give a twisted real join at each point with a datum of $N$, a datum of position $\mathrm{RX}$ and a pinned column. By the last hypothesis, the datum of $N$ gives a datum of the extension with law. For the extension with law, the twisted real join exists by the published inputs of the third layer, the membership statement at layer points and the pinned column. The change of $N$ is carried under the quantifier over large contexts. $\square$

So the export of built cores reduces to the inputs at a datum and to the twist theorem for all powers. Section 5 proves the first.

**Remark 6.4.8 (Formalization).** The theorems are at [AutomorphyOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AutomorphyOfHyp.lean#L27) (the second name at line 44), [SExport.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SExport.lean#L20), [ExportAtBundlesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtBundlesStatement.lean#L16), [ExportAtBundles.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtBundles.lean#L16), [ExportAtOfBundlesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtOfBundlesStatement.lean#L16) and [ExportAtOfBundles.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportAtOfBundles.lean#L17). The names `automorphy_of_hypotheses_alt_alt`, `series_realization_of_published_alt`, `realization_of_published_alt`, `exportAt_bundles_alt` and `exportAt_of_bundles_alt` do not describe their statements: no automorphy, realization, published result or bundle appears in them. The second names are proved by `first | exact … | …` with identical types. `automorphy_of_hypotheses_alt_alt` allows any `SExt` and `GeoP`, but its caller uses only `SExt.none` and `geoCl anyGeometry`. In the proof of `exportF_isBuiltE_alt_alt` the pattern `⟨b, -⟩` drops the condition `EntC b.ker`, so the "E" of `IsBuiltE` is never used. The twisted real join is `TwistedRealJoin` ([TwJoin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TwJoin.lean#L46)), and the passage from the extension with law to it is `nonempty_twOf_of_extensionWithLaw`, which we did not open. The hypothesis `HeckeInt` lives in the namespace `UnusedSlot39`, yet it is used in `exportAt_bundles_alt`. The first conjunct of `SetHyp` is `True` ([BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L327)). Each theorem copies a version without "alt" that has `GalSide` and `GalHodge` in place of `GalSideAlt` and `GalHodgeN`. We did not unfold `GoodTw`, `FullRk`, `BasisOf`, `SgJ`, `Built`, `RealSide`, `SerSide`, `FieldOk` beyond the two fields used, or `Conclusion5`; the phrase "the conclusion of step 5" translates the last name only.
