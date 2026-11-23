---
id: det-line-trivial-of-toroidal
title: The Lie determinant line has a flat section, from a toroidal compactification
kind: theorem
decl: GlobalTheory.DetLine.detLineTrivial_of_toroidal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DetLineTrivialOfToroidal
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem proves `DetLineTrivial` from the quoted existence of toroidal compactifications. `DetLineTrivial` says that on a closed component of the moduli space there is a flat rule on Lie eigenbases that vanishes nowhere and is unique up to a constant. The name suggests a section of a determinant line. The theorem sits below the covolume bound [topCovolG_alt_alt](/entry/top-covol-g-alt-alt/). Its callers pass the field `p1` of [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/) as the hypothesis. Below this theorem are 358 declarations.

## Statement

Take a CM field $E$ with a host $H$, a datum $D$ of signature $(p, q)$, a level $l$, a moduli space $X_o$ and coefficients $c$. Let $U$ be an open and closed subset of the generic fibre $X_{o,F}$, geometrically connected over $c.F$. Let $\tau : E \to \mathbb{C}$ with $\tau(\mathrm{rt}) = \mathrm{rt}_0$. A rule $\sigma$ (`Rule`) assigns a value to a point $x$ with an eigenbasis $v$ of the Lie algebra for the character $\chi = \tau$ and an eigenbasis $w$ for $\bar\tau$. `IsSection` asks that $\sigma$ is compatible with base change and that $\det N \cdot \sigma(v, w) = \det M \cdot \sigma(Mv, Nw)$.

**Theorem.** Assume `ToroidalCompactification`. Then for all such data:

1. `HasTransport` holds at each embedding $e : c.F \to \mathbb{C}$;
2. there is a rule $\sigma$ on $U$ that is a section, vanishes nowhere and is flat at each $e$ (`IsFlatAt`);
3. every flat section $\sigma'$ is $a\sigma$ for a unique $a \in c.F$;
4. for each model $Y$ of $X_o$ with a normal generic fibre, there is a nowhere vanishing section $\sigma_b$ on the closure of $U$ in $Y$ that restricts to $\sigma$, and every section there is a unique multiple of $\sigma_b$.

## Proof

1. If $p + q = 0$, the eigenbases are empty and all determinants are $1$. The rule $\sigma = 1$ works, and `hasMarkingPreservingTransport_of_rank_zero` gives the transport (`exists_of_rank_zero`).
2. If $p + q \ge 1$, the hypothesis gives a model $Z$ with smooth generic fibre of relative dimension $\dim D$ and a boundary with simple normal crossings. Then `exists_of_snc` builds the section. It compactifies the component (`exists_variety_compactifying_connected_component`). At each good embedding it takes a family from `closing_of_abelianSchemeLaws` with period lattice bases of the same signature (`exists_hermitianPeriodLatticeBasis_same_signature`). It gets a nowhere vanishing section on $Z$ from a horizontal function (`exists_nonvanishing_detLine_section_of_horizontal`). It restricts this section to $U$, shows flatness by comparing with period determinants (`isFlat_of_const_mul_periodDeterminant`), and extends it to normal models (`exists_nonvanishing_extension_normal_compactification`). At an embedding that is not good, it uses the conjugate embedding (`good_or`).
3. Uniqueness on $U$ is `flat_unique`. It uses flatness only at the given embedding of $c.F$ into $\mathbb{C}$.
4. Uniqueness on the closure is `cpt_unique`. It uses `exists_constant_function_normal_compactification`.

## In the Lean code

The theorem is at [DetLineTrivialOfToroidal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DetLineTrivialOfToroidal.lean#L182). `DetLineTrivial` is at [HermitianCompactForm.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/HermitianCompactForm.lean#L163).

- The hypothesis `ToroidalCompactification` is not used when $p + q = 0$.
- A second definition named `DetLineTrivial` is in `FramedFlatCoordinates.lean` at line 185. The theorem proves the one in `HermitianCompactForm.lean`.
- We have not unfolded the cited `T.` lemmas, `HasTransport`, `IsFlatAt` or `Restricts`. The steps above describe them by their names and their place in the proof.
