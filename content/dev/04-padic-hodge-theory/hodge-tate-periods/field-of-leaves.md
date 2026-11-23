---
id: field-of-leaves
title: The l-adic character of a Hecke character is de Rham, from two period facts
kind: theorem
decl: PositivityTheory.SecR.Hladr2.field_of_leaves
module: Development.WeilBound.CoreStatements.HeckeCharacterDeRham.DeRhamHeckeResults.LAdicHeckeDeRham.LAdicHeckeFields.FieldOfLeaves
covers: 415
status: drafted
drafted_by: writer@claude
---
This theorem proves `HeckeLAdicCharacterDeRham` from two hypotheses about periods of Lubin-Tate characters, `TiltLeaf` and `ProductLeaf`. Its one caller is [field_outright](/entry/field-outright/), which supplies both hypotheses. So the result holds there without assumptions.

## Statement

`HeckeLAdicCharacterDeRham` says: let $\chi$ be an algebraic Hecke character of a number field $E$ with type $n$, and let $\mu$ be its $l$-adic Galois character. Then at each finite place $w$, the restriction of $\mu$ to the decomposition group is de Rham (`IsdRAt`), with the single Hodge-Tate jump $-n(\iota \circ \tau)$ at each embedding $\tau$ (`IsJumpsAt`). We have not unfolded `IsdRAt` and `IsJumpsAt`.

The two hypotheses concern a finite extension $K$ of $\mathbb{Q}_l$ with uniformizer $\pi$, a character $\chi$ of the Galois group of $K$, and an embedding $\mu$ of $K$:

- `TiltLeaf`: given Lubin-Tate data (`LTData`) for $\chi$ with torsion points $z_n$, there is a nonzero system $v_n$ in the tilt with $v_{n+1}^q = v_n$, on which Galois acts through the Lubin-Tate power series, with $\theta(v_n)$ close to $z_n$ when $\mu$ is the inclusion.
- `ProductLeaf`: if $N_{K/\mathbb{Q}_l}\chi$ equals the cyclotomic character on the elements that fix the unramified closure, then each family of pre-periods $t_\mu$ (`PrePer`) has $t_\mu \notin \mathrm{Fil}^2$ when $\mu$ is the inclusion, and $t_\mu \notin \mathrm{Fil}^1$ otherwise.

**Theorem.** `TiltLeaf` and `ProductLeaf` imply `HeckeLAdicCharacterDeRham`.

## Proof

The proof is `field_of_ltPeriods` applied to `hasPeriods_main HT HP`. The lemma `field_of_ltPeriods` reduces the statement to `LTPeriods`: each Lubin-Tate character (`IsLTChar`) that is continuous has periods (`HasPeriods`). That is, for each $\mu$ there is $y \in B_{\mathrm{dR}}$ with $g y = \mu(\chi(g))\,y$, and $y \in \mathrm{Fil}^1 \setminus \mathrm{Fil}^2$ when $\mu$ is the inclusion, $y \in \mathrm{Fil}^0 \setminus \mathrm{Fil}^1$ otherwise.

`hasPeriods_main` builds $y$. `lubin_tate_norm_cyclotomic` gives the norm condition of `ProductLeaf`. `pre_period`, from `TiltLeaf`, gives a pre-period $t_\mu$ in $B_{\mathrm{dR}}^+$. `ProductLeaf` gives the "not in" halves, and `fil_iff` moves the filtration from $B_{\mathrm{dR}}^+$ to the ring of `HasPeriods`. The two leaves carry the content. This theorem only joins them.

## In the Lean code

The theorem is in [FieldOfLeaves.lean](lean:Development/WeilBound/CoreStatements/HeckeCharacterDeRham/DeRhamHeckeResults/LAdicHeckeDeRham/LAdicHeckeFields/FieldOfLeaves.lean#L273), with `TiltLeaf` at line 30 and `ProductLeaf` at line 41. `LTPeriods` and `field_of_ltPeriods` are in [Reduce.lean](lean:Development/WeilBound/CoreStatements/HeckeCharacterDeRham/DeRhamHeckeResults/LAdicHeckeDeRham/LAdicHeckeFields/Reduce.lean#L159). `IsLTChar` and `HasPeriods` are in [HasPeriods.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/HasPeriods.lean#L21). The caller passes `LTPer.Tilt.tilt_period` and `lubin_tate_period_not_filtered` in `PublishedTheorems/HeckeLAdicCharacters/Outright.lean`.
