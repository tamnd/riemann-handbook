---
id: plug-comp
title: The total volume of the fundamental sets is at most the level mass
kind: theorem
decl: MainStatements.Tam.Plug.comp
module: Development.WeilBound.RepresentationTheoryGL.TubeMeasures.DisjointTubes.ConstantSupremum.Imports
covers: 468
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem bounds the sum, over the components $X_k$ of a family of data, of the volumes of fundamental sets in the frame space. The bound is the explicit number $\mathrm{massLev2}(E, r, M)$. Its only caller is the [local volume factor](/entry/tamagawa-local-volume-factor/), where this number becomes a factor of the constant in the bound of the sup norm by the Petersson norm. The theorem is a pass-through: it applies the reduction `MainStatements.Tam.comp` to four proved statements.

## Statement

Let $D$ be a datum (`D7`) with CM field $E$, $d = [E:\mathbb{Q}]$, rank $r$, and a level whose integer is $M$. Let $\sigma$ be an embedding of the coefficient field, let $X_k$ be the components of the data `U σ`, and suppose that the conditions `Laws` and `GoodEmb` hold (we have not unfolded them). For each $k$ let $x_k$ be a frame whose Gram matrix at each place is diagonal with entries $\pm 1$ (`IsOrth`), and let $F_k$ be a fundamental set for the arithmetic group and the Borel action (`IsFundSet`: measurable, injective modulo the action, and covering almost everywhere). Let $\mu_k$ be the measure `muF`, Lebesgue measure on the chart, restricted to the domain, with the density `densF` (a product over places of inverse squared norms; we have not unfolded its terms). Then

$$\sum_k \mu_k(F_k) \le M^{d r^2}\, 15^{d r^2} \bigl(3\, d^2 r^4 \lvert \mathrm{disc}\, E \rvert^{2/d}\bigr)^{3 d r^2}.$$

This is the statement `CompSt`.

## Proof

The term is `comp (tube0 vol stab idx) num`. Here `tube0` is a second name for `MainStatements.Tam.tube`, which turns the volume, stabiliser and index statements `VolSt`, `StabSt`, `IdxSt` into the tube bound `TubeSt`. The theorems `vol`, `stab`, `idx` and `num` prove those statements and `NumSt`, so no hypothesis remains.

The work is in `MainStatements.Tam.comp`. It calls `C.sum_muF_le`, which uses `TubeSt` to give the bound $16^{f r^2} M^{2 f r^2}\, \mathrm{vol}(U_r)^f\, \mathrm{massI}(D, r)$ with $d = 2f$. Then `NumSt` gives $\mathrm{vol}(U_r) \le 13^{r^2}$, `mass_stdLat_le` bounds `massI` by the last factor above, and $16 \cdot 13 \le 15^2$. The rest is bookkeeping.

## In the Lean code

- The theorem: [Imports.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/ConstantSupremum/Imports.lean#L17).
- `CompSt`: [CompSt.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/CompSt.lean#L14); `massLev2`: [MassLev2.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/MassLev2.lean#L13).
- `MainStatements.Tam.comp`: [SumMuFLe.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/MeasureSumBounds/SumMuFLe.lean#L110).
- `tube0`: [Tube0.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/ConstantSupremum/Tube0.lean#L3), with the same type as `tube` and the proof `tube`.

The file is named `Imports`, but it holds four theorems: `up`, `low`, `comp` and `size`. Each one plugs the proved statements into a reduction.
