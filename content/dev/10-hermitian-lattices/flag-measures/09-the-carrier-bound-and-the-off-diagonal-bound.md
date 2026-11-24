---
title: The carrier bound and the off-diagonal bound
decls:
  - GlobalTheory.carrierNeedsFromD
  - GlobalTheory.CarrierGap.carrierP
  - GlobalTheory.CarrierGap.theoremS_leaves_of_carrierG
  - GlobalTheory.CarrierGap.offDiag
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The carrier bound and the off-diagonal bound

This section proves the off-diagonal bound for the spectral ties of a selection: for distinct words $u \ne u'$ the off-diagonal entry $K_0(u, u')$ satisfies
$$\|K_0(u, u')\|^2 \le (1 + b^{-6}) \frac{d(u)\, d(u')}{D^\ast}.$$
The bound comes from Theorem S, whose hypotheses are collected here, and the row bounds of the eighth section. One hypothesis of Theorem S, the carrier bound, is proved here with no hypothesis from three earlier results. The off-diagonal bound is part 2 of [the choice of spectral ties](/entry/at-choice-alt/).

### The carrier inputs

The carrier bound needs three results proved earlier in the volume.

1. *Theorem P in compact form* ([the compact theorem](/entry/actual-compact-theorem/)): for real place data, level data and $1 \le l_0 \le k$ there are submodules $K(l)$ of the radical space with the properties of Theorem P, and every compactly supported function in the right classes, bounded below on its support, has a representative in $K(0)$ on the relevant domain.
2. *Model places* ([the model place theorem](/entry/model-place-built-holds/)): there is a constant $C_c$ such that each built place with constant $C_c$, for each CM field and under the place and word conditions, has a model place at each infinite place.
3. *Built bounds* ([the built bounds](/entry/pb-built-bounds2-cpt/)): if Theorem P in compact form holds, then for each $C_b$ there are constants $C_c$ and $C_4 \ge 1$ such that each leading form setting satisfies a list of bounds that ends with the concrete sum form.

**Theorem 3.9.1 (Carrier inputs).** The three statements above hold together.

Lean: `GlobalTheory.carrierNeedsFromD`.

*Proof.* Each part is one of the three results. $\square$

Part 3 is an implication with the hypothesis of part 1. So with part 1 it is the same as its conclusion.

### The carrier bound

**Definition 3.9.2 (Carrier bound).** The *carrier bound* is the statement: there are $C_4 \ge 1$ and $C_{A,0}$ such that for each $C_A \ge \max(C_{A,0}, 1)$ and constants $C_0 \ge 1$, $C_G \ge 0$, $C_\Delta > 4$, $c_T > 0$, $C_b > 0$ with $c_T C_b > 1$ there is $k_0$ with this property. For all further positive constants there are thresholds $C'_0$ and $C_{l,0}$ such that for $C' \ge C'_0$ and $C_l \ge C_{l,0}$ the full carrier condition with $C_4$ and $C_A$ holds for each datum $D$, size data, spectral ties and words $u \ne u'$, under these conditions: $D$ has ties, $k \ge k_0$, the standing hypothesis, agreement of the infinite places with the ties, the size hypothesis, equal base indices, a point representation and the pin condition.

The full carrier condition asks for local spaces at each infinite place, a Hida setting and level towers, with bounds in terms of $C_4$ and $C_A$.

**Theorem 3.9.3 (Carrier bound).** The carrier bound holds.

Lean: `GlobalTheory.CarrierGap.carrierP`.

*Proof.* The proof has four steps.

1. The theorem on carrier inputs gives Theorem P in compact form, the model places and the built bounds.
2. There is a constant $C_b$ with the lift property at level $3$.
3. The $K$-finite vectors are dense and not zero. With the uniqueness of Bessel maps for large gaps, this gives the pins of the side, and from the pins the leaves of the side. The leaves give the positive side bound for $C_b$.
4. The carrier bound follows from the compact model of the carrier inputs, the side bound and [the model lemma](/entry/lemma-model/). $\square$

### The hypotheses of Theorem S

Theorem S has nineteen hypotheses. They are: a local model, density inputs, row inputs for each datum, the row bound, an off-diagonal kernel condition, the carrier bound, agreement of the kernel exponents, a folding condition, an integral condition, absolute convergence, finiteness of the cells, the decay of the Whittaker functions for large gaps, choices, a formula, a sum of rows, the row form for all data, mass data, a link condition and a split condition.

**Theorem 3.9.4 (Hypotheses of Theorem S).** Assume the carrier bound, the row bound, the finite dimension of rows, the uniqueness of Bessel maps for large gaps (two smooth Bessel maps of a discrete series with gap $h \ge 120 n^3$ are proportional) and the Siegel-Weil condition at each Hida setting. Then the nineteen hypotheses of Theorem S hold.

Lean: `GlobalTheory.CarrierGap.theoremS_leaves_of_carrierG`.

*Proof.* Each hypothesis comes from one result.

1. Thirteen of them are proved with no hypothesis, among them the local model, the density inputs, the off-diagonal kernel condition, the agreement of the kernel exponents and the formula.
2. The row inputs come from the deep cut leaves ([the deep cut](/entry/cut-leaves-deep-outright/)) through [the row datum from the deep cut](/entry/rows-datum-p-of-deep/) and two further reductions.
3. The uniqueness of Bessel maps gives the decay of the Whittaker functions, and with the density of $K$-finite vectors it gives the independence at all places.
4. The Siegel-Weil condition gives the normalizing constants and the mass data.
5. The finite dimension of rows and the decay give the finiteness of the cells.
6. The carrier bound and the row bound are hypotheses as they are. $\square$

### The off-diagonal bound

Let $\mathcal C$ be a family class and $s$ a selection for $\mathcal C$: for each family $F$ in $\mathcal C$ a threshold $x_0$ and spectral ties $s(F, x, i)$ for each large $x$ and each index $i$. For words $u, u'$ let $K_0(u, u')$ be the sum of the identity, generic and non-generic parts of the term of the ties for $(u, u')$, let $d(u)$ be the degree of $u$, let $D^\ast$ be the main term and let $b$ be the scale of the size data.

**Theorem 3.9.5 (Off-diagonal bound).** Assume the Siegel-Weil condition at each Hida setting, the row bound, the finite dimension of rows, the local tie condition at each finite place for each selected datum, the rank bound of level $3$ on $\mathcal C$ and the loop row statement of level $3$ for $\mathcal C$ and $s$. Then it is [closed](/step/closed-def/) on $\mathcal C$ that, eventually and under the size hypothesis with $C_0 = 3$, for each $x$ above the threshold, each $i$ and all words $u \ne u'$,
$$\|K_0(u, u')\|^2 \le (1 + b^{-6}) \frac{d(u)\, d(u')}{D^\ast}.$$

Lean: `GlobalTheory.CarrierGap.offDiag`.

*Proof.* The proof has three steps.

1. The rank bound gives a frame bound. With the finiteness of the cells and the local tie condition, each selected tie satisfies, eventually, the seven conditions of a good tie.
2. The carrier bound and the uniqueness of Bessel maps are proved, so the theorem on hypotheses of Theorem S applies. [Theorem S](/entry/theorem-s-of-conj/) gives a bound on $K_0$, and its bound is kept for distinct words.
3. Combine this bound with step 1, the size rows, the size bound of level $3$, the loop rows and the absolute convergence of the tied series. This gives the bound of the theorem. $\square$

The constant $1 + b^{-6}$ is close to $1$: the off-diagonal entries are, up to this factor, at most the geometric mean of the diagonal sizes $d(u)/\sqrt{D^\ast}$ and $d(u')/\sqrt{D^\ast}$.

**Remark 3.9.6 (Formalization).** The carrier inputs are the three statements `ThmPActualCpt`, `ModelPlaceBuilt2` and `BuiltBounds2Cpt`, proved by `actual_compact_theorem`, `model_place_built_holds` and `pb_builtBounds2Cpt`; the conjunction is the statement `CSTarget4` written out, but the theorem does not use that name. The carrier bound is `CarrierP` (TheoremSClosedP.lean, line 20) and the full carrier condition is `CarrierFull`, not unfolded here. The proof of `carrierP` (OffK0Closed.lean, line 665) uses `liftAt3_exists`, `kFinDense_holds`, `xPinsP_ofG`, `xLeavesP_of_pinsPG`, `carrierXSideP_of_leaves` and `carrierP_of_compact_model`, and it is a near copy of `carrierP_of_kfin4` (CarrierXPinsP.lean, line 318). The nineteen hypotheses are `TheoremSClosedHypotheses` (TheoremSConclusion.lean, line 58); another definition with the same name in ThmSOwn.lean (line 983) is a conclusion, not a list of hypotheses. The uniqueness of Bessel maps is `UniqGap`, proved by `uniqGap_holds`, and the row bound is `RowNGP`. The off-diagonal bound is `TheoremSSelected` and is proved at OffK0Closed.lean, line 673, through `hTF_of_ranks`, `selOK_of`, `theoremS_of_conj`, `theoremS_distinct_of_closed` and `offDiagonalK0_of_rows`. The theorem on hypotheses of Theorem S is at OffK0Closed.lean, line 633; the nine `Fact` instances of its section are supplied by global instances.
