---
title: Spectral objects over replaced stages
decls:
  - GlobalTheory.Mem.SRe.exists_sRest_top
  - GlobalTheory.T.exists_spectralLevel_objects_replacedStages
  - GlobalTheory.Mem.SRe.satOfDiscreteSeries
  - GlobalTheory.T.exists_spectralObjects_over_replacedStages
  - GlobalTheory.Mem.SRe.UpS.satOfDiscreteSeries
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Spectral objects over replaced stages

In this section we use the finite point of the previous section to build the spectral objects that the fourth level needs. These objects are a point $t$, a constant $c > 0$, and an isometry $j$ from the column space $E$ of the tower datum onto a space of evaluated rows. We then show that these objects stay valid when we replace the S-datum of a late stage by the new datum that $j$ makes. The analytic inputs are five standard facts about discrete series and automorphic forms. We take them as given and name them below.

**Setting.** Let $D$ be a tower datum. Let $R$ be realisation data for $D$, with face $F$. For each word $u$ of $D$, let $F_0(u)$ be a degree-zero form. It has a level class $\mathrm{lev}(u)$, a value $y(u)$ and a value vector $e_Y(u)$. Let $E$ be the column space of $D$ and let $H_E$ be the Hilbert space of $R$. Let $e_E \colon E \to H_E$ be a complex linear map.

**Definition 1.2.1 (Spectral pack).** A *spectral pack* $P$ for $(D, F_0)$ is a Hida setting $X$ for $D$ together with these data: an adelic bridge isomorphism; a full choice $Y$ of sharp data for $X$ with the finiteness property $\mathrm{Fin}(Y)$; the standard additive character $\psi$ of $\mathbb{A}_F$ with the measure tie for it; a transport map for each word $u$; the column dictionaries (into, bijective, level and isometry parts); the equality of the automorphic instance of $X$ with the instance of $D$; a good operator $G$ on $X$; and the pin that makes $\iota_E$ the identity. The finiteness property $\mathrm{Fin}(Y)$ says that each sharp map is bijective, takes values in $\mathrm{HH}(X)$ and is linear, that $\mathrm{HH}(X)$ is finite dimensional, and that each fibre of the row transports is finite.

**Definition 1.2.2 (Spectral restriction).** Let $P$ be a spectral pack and let $\mathrm{EEC}(X, G)$ be the space of evaluated columns of $X$ for the good operator $G$. A *spectral restriction* $S$ of $P$ is an isomorphism from the S-datum of $D$ to the S-datum $s(P)$ that $\mathrm{Fin}(Y)$ makes, together with an automorphism tie, a column pin, a linear isometry
$$j_S \colon E \xrightarrow{\ \sim\ } \mathrm{EEC}(X, G),$$
a row pin, and a local tie.

**Definition 1.2.3 (New datum and replacement).** Let $P$ be a spectral pack, let $D_{\mathrm{all}}$ be the total dimension of $D$, and let $h_D$ be a proof that $\dim_{\mathbb{C}} \mathrm{HH}(X) = D_{\mathrm{all}}$. For a linear isometry $j \colon E \to \mathrm{EEC}(X, G)$, the *new datum* $P^{\mathrm{new}}(h_D, j)$ is the S-datum $s(P)$ with the column dictionaries of $P$, the equality $h_D$, and the map $E \to \mathrm{HH}$ that is $j$ followed by the conjugate inclusion. A *replacement* of $D$ is a triple $Z = (Z_s, N, h)$ with $Z_s$ a new datum, $N_u$ a submodule of the $\mathcal{O}_L$-lattice of the word $u$, and $h$ a real weight on words. It gives a replaced datum $D_Z$ and a replaced full choice $Y_Z$. Forms $F'$ on $D_Z$ have the *same levels and values* as $F_0$ when $F'(u)$ and $F_0(u)$ have the same level class, the same value $y$ and the same value vector $e_Y$ for each word $u$.

**Definition 1.2.4 (Evaluation tie and row tie).** Let $t$ be a point of the adelic group of $D$ and let $c > 0$. For a unit vector $v_0$ of the lowest $K_\infty$-type and a form $S$, write $\mathrm{ev}_{v_0} S$ for the function $g \mapsto \langle S(g), v_0 \rangle$. The *evaluation tie* $\mathrm{EvTie}(t, c)$ says that there are a unit vector $v_0$ and a linear isomorphism $J$ from the level space onto $\mathrm{EEC}(X, G)$ with
$$\begin{aligned} J S &= \bigl(x \mapsto \mathrm{ev}_{v_0} S(\iota_X^{-1}(x)\, t)\bigr) \text{ almost everywhere}, \\ \lVert J S \rVert^2 &= c\, \langle S, S \rangle. \end{aligned}$$
The *row tie* $\mathrm{RowJ}(t, j)$ says that there are a unit vector $v_0$ and $a > 0$ with
$$j(x) = a \cdot \mathrm{ev}_{v_0}\bigl(e(e_E x)\bigr)(\iota_X^{-1}(\cdot)\, t)$$
almost everywhere, for each $x \in E$.

**Definition 1.2.5 (S-object).** An *S-object* for $(R, F, e_E, F_0)$ is a spectral pack $P$, a spectral restriction $S$ of $P$, a point $t$, a constant $c > 0$, a proof that $t$ sees the row level (section 1), the evaluation tie $\mathrm{EvTie}(t, c)$, and the row tie $\mathrm{RowJ}(t, j_S)$.

### The analytic inputs

We use five statements as hypotheses. Each is a standard fact. The sources are in the Notes at the end of the chapter.

- **(DS)** A discrete series representation with Harish-Chandra parameter $\lambda$ has infinitesimal character $\lambda$.
- **(HC)** For a fixed $K_\infty$-type, a fixed open compact level $U$ and fixed infinitesimal character data, the space of automorphic forms of that type is finite dimensional.
- **(RD)** A smooth cusp function of uniform moderate growth is of rapid decay.
- **(DU)** Two discrete series representations with the same parameter are unitarily equivalent.
- **(RF)** Let $R$ be the right regular representation on $L^2$ of the automorphic quotient, and let $e$ be a locally constant function supported in the level. Then the image of the convolution operator of $e$ against a discrete series matrix coefficient is finite dimensional.

The background is in Volume 1, at [discrete series](/learn/representations/#discrete-series) and [constant terms and cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms).

### The hypotheses on the stage

We also use these hypotheses on $D$, $R$, $F$, $P$ and $e_E$.

- **(G)** The gap condition: $r \geq 1801$, and consecutive entries of each Harish-Chandra parameter of $D$ differ by at least $16 r^{19}$.
- **(I)** The test function $\phi$ of $X$ is integrable for the archimedean measure $\mu_\infty$.
- **(L)** The local tie: at each place $p$ of $F$, the local S-datum of $D$ is isomorphic to the local model.
- **(T)** The real tie: the scale, the signs and the volumes of $D$ are the true ones.
- **(S)** The dual lattice $D^*$ of $D$ is the standard one.
- **(R1)** to **(R7)** The row hypotheses: $R$ has the level character of the family; $R$ has the group levels for $F$; $R$ has a group pin; $R$ models the tower; the range of $e_E$ is the preimage under $e$ of the level space at the true level; $\lVert e_E x \rVert^2 = n_P\, \lVert x \rVert^2$, with $n_P$ the true norm of $F$; and $D_{\mathrm{all}}$ is the dimension of the multiplicity space.
- **(E)** The idempotent $e_0$ of $D$ has real coefficients.

**Theorem 1.2.6 (Spectral restriction at the top stage).** Assume (DS), (HC), (RD), (DU) and (RF). Let $P$ be a spectral pack for $(D, F_0)$ and assume (G), (I), (L), (T), (S), (R1) to (R7) and (E). Then there are a proof $h_D$ that $\dim \mathrm{HH}(X) = D_{\mathrm{all}}$, a linear isometry $j \colon E \to \mathrm{EEC}(X, G)$, a point $t$ and a constant $c$ with these properties.

1. $c > 0$, and $t$ sees the row level.
2. The evaluation tie $\mathrm{EvTie}(t, c)$ holds.
3. The row tie $\mathrm{RowJ}(t, j)$ holds.
4. Let $Z = (P^{\mathrm{new}}(h_D, j), N, h)$ be a replacement, and let $F'$ be forms on $D_Z$ with the same levels and values as $F_0$. Then $\mathrm{Fin}(Y_Z)$ holds, and the replaced pack $P_Z$ has a spectral restriction $S$ with $j_S = j$ followed by the column identification of $Z$.

Lean: `GlobalTheory.Mem.SRe.exists_sRest_top` (also `GlobalTheory.T.exists_spectralLevel_objects_replacedStages`, a second name).

*Proof.* We build the objects in six steps.

*Step 1: the point.* By the theorem on a finite point that carries the row level (section 1), applied with (R1), (R2), (R3) and (E), there is a finite point $t$ that sees the row level.

*Step 2: the lowest vector.* The lowest vector evaluation theorem uses (DS), (RD), (DU), (RF), (G), the archimedean and lowest-type parts of (R4), and the point $t$. It gives a unit vector $v_0$ and a constant $c > 0$ such that $S \mapsto \mathrm{ev}_{v_0} S(\iota_X^{-1}(\cdot)\, t)$ maps the level rows onto the conjugated rows, and multiplies norms squared by $c$.

*Step 3: the good rows.* The evaluation of step 2 sends the good rows of the face $F$ to the conjugated good rows. This gives an evaluation map on the good rows of $F$ with values in $\mathrm{EEC}(X, G)$, and it gives the evaluation tie $\mathrm{EvTie}(t, c)$.

*Step 4: the level columns.* By (HC) and (RD), the level space at the true level of $F$ lies in the level space at the trivial level. (The same theorem also says that this space is finite dimensional. We do not use that part.)

*Step 5: the row isometry.* The row isometry theorem uses $c > 0$, the unit vector $v_0$, the model part of (R4) for $H_E$, the range and norm conditions (R5) and (R6), step 4, and the evaluation of step 3. It gives two things. First, if $D_{\mathrm{all}}$ is the dimension of the multiplicity space, then $\dim \mathrm{HH}(X) = D_{\mathrm{all}}$. Second, it gives a linear isometry $j$ with $\mathrm{RowJ}(t, j)$. In this step, $j$ is the evaluation of step 2 composed with $e_E$ and scaled by $a = (c\, n_P)^{-1/2}$. Then (R6) and the norm identity of step 2 give
$$\lVert j(x) \rVert^2 = a^2\, c\, n_P\, \lVert x \rVert^2 = \lVert x \rVert^2.$$
By (R7) the first part applies, and we get $h_D$.

So parts 1, 2 and 3 hold. For part 4, let $Z$ and $F'$ be as stated.

*Step 6: the replaced stage.* The finiteness property passes from $Y$ to the replaced full choice, so $\mathrm{Fin}(Y_Z)$ holds. The restriction theorem for replaced stages uses $\mathrm{Fin}(Y_Z)$, (I), (L), (T) and (S). It gives a spectral restriction $S$ of $P_Z$ with $j_S = j$ followed by the column identification of $Z$. $\square$

The column identification of $Z$ is the identity isometry. Thus $j_S$ is the map $j$ of the theorem.

### Late stages

A late stage carries its own tower datum. We now restate the theorem for the stage that we get when we replace the S-datum of a late stage.

**Definition 1.2.7 (Relabelled late stage).** Let $a$ be a late stage with weight $W$, column side $V$, stage $\mathrm{st}$, lattice data $N$ and group data $G$. Let $Z$ be a replacement of the tower datum $D(a)$ of $a$. The *relabelled stage* $a_Z$ is
$$a_Z = \bigl(W,\ V_Z,\ \mathrm{st}_Z,\ N,\ G\bigr),$$
where $V_Z$ is the column side with the S-datum of $Z$ and $\mathrm{st}_Z$ is the stage that $Z$ replaces. Its tower datum is the replaced datum $D(a)_Z$. Its Hida setting is the replaced Hida setting $X_Z$, and the good operator, points and isometries of $a$ carry over to $a_Z$ without change. Forms $F_1$ on $D(a_Z)$ have the *same levels and values* as $F_0$ when they do so as forms on $D(a)_Z$. An *S-object over* $a_Z$ is an S-object for the realisation data and face of $a_Z$ that $R$ and $F$ give.

**Theorem 1.2.8 (S-objects over replaced late stages).** Assume (DS), (HC), (RD), (DU) and (RF). Let $a$ be a late stage, and let $R$, $F$, $F_0$, $e_E$ and a spectral pack $P$ be given for $D(a)$. Assume (G), (I), (L), (T), (S), (R1) to (R7) and (E) for $D(a)$. Then there is a new datum $Z_s$ for $D(a)$ with this property. For each choice of $N$ and $h$, and for each set of forms $F_1$ on $D(a_Z)$ with the same levels and values as $F_0$, where $Z = (Z_s, N, h)$, there is an S-object for $(R, F, e_E, F_1)$ over $a_Z$.

Lean: `GlobalTheory.Mem.SRe.satOfDiscreteSeries` (also `GlobalTheory.T.exists_spectralObjects_over_replacedStages`, a second name).

*Proof.* Take $h_D$, $j$, $t$ and $c$ from the theorem on the top stage, and put $Z_s = P^{\mathrm{new}}(h_D, j)$. Let $N$, $h$ and $F_1$ be given, and let $Z = (Z_s, N, h)$. The forms $F_1$ are forms on $D(a)_Z$ with the same levels and values as $F_0$. Part 4 of the theorem gives $\mathrm{Fin}(Y_Z)$ and a spectral restriction $S$ of $P_Z$ with $j_S = j$ followed by the column identification.

We now move each object to $a_Z$. The tower datum of $a_Z$ is $D(a)_Z$ by definition, so each move is the identity on the underlying data. The pack $P_Z$ becomes a spectral pack over $a_Z$. The restriction $S$ becomes a restriction of that pack, with the same isometry. The point $t$ stays the same. The facts that $t$ sees the row level, the evaluation tie, and the row tie for $j$ move in the same way. The equality for $j_S$ lets us rewrite the row tie for $j$ as the row tie for $j_S$. These objects, with $c > 0$, form the S-object over $a_Z$. $\square$

**Definition 1.2.9 (Row package and row hypotheses).** A *row package* $p$ for $D$ is a finite group $G'$, index types, a family $A$, a number field $K_s$ with an algebra map to $L$, realisation data $R$, a face $F$, and a map $e_E$. The *row hypotheses* $\mathrm{RowHyp}(p)$ are (R1) to (R7) for $R$, $F$ and $e_E$.

**Corollary 1.2.10 (The saturation statement).** Assume (DS), (HC), (RD), (DU) and (RF). Let $a$ be a late stage, $p$ a row package for $D(a)$, $F_0$ forms on $D(a)$ and $P$ a spectral pack for $(D(a), F_0)$. Assume (G), (I), (L), (T), (S), (E) and $\mathrm{RowHyp}(p)$. Then there is a new datum $Z_s$ for $D(a)$ such that, for each $N$, $h$ and forms $F_1$ on $D(a_Z)$ with the same levels and values as $F_0$, there is an S-object for $(p.R, p.F, p.e_E, F_1)$ over $a_Z$, with $Z = (Z_s, N, h)$.

Lean: `GlobalTheory.Mem.SRe.UpS.satOfDiscreteSeries`.

*Proof.* Split $\mathrm{RowHyp}(p)$ into (R1) to (R7) and apply the theorem on replaced late stages to the data of $p$. $\square$

The corollary is the input that the step from level three to level four uses. That step is the theorem [level four from level three](/entry/has4-of-has3-of-s-ext-none/). There, a late stage at level three gives a new datum $Z_s$ by the corollary. The stage that $Z_s$ replaces has S-objects for every choice of columns, and the level-three condition then lifts it to level four.

**Remark 1.2.11 (Formalization).** Two theorems have the name `satOfDiscreteSeries`, one in `GlobalTheory.Mem.SRe` and one in `GlobalTheory.Mem.SRe.UpS`. The second ([LevelThreeToFour.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelThreeToFour.lean#L68)) is a single term that splits the seven row hypotheses and calls the first through its second name. In the top-stage theorem only the first half of the level-column lemma is used. Its finite-dimensionality half is not used ([ExistsSpectralLevelObjectsReplacedStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralLevelObjectsReplacedStages.lean#L30)). The column identification `eEECre` is the identity isometry, so the equality for $j_S$ says that $j_S = j$ in substance. The moves to the relabelled stage are casts: `packL`, `restL`, `tL`, `mvSee`, `mvEv_holds` and `mvRowJ` are each the identity on terms, checked with `with_unfolding_all` ([ExistsSpectralObjectsOverReplacedStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralObjectsOverReplacedStages.lean#L42)). The gap condition (G) is the definition `GapHyp` with the explicit constants $1801$ and $16 r^{19}$. The five analytic inputs enter as hypotheses of type `Prop` (`DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesUpqUnique`, `RowsFinDim`) and are not proved in the library.
