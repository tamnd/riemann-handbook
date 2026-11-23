---
id: arith-hilbert-samuel-of-ample-hs
title: The nef Hilbert-Samuel formula from an upper and a lower bound
kind: theorem
decl: GlobalTheory.HSNef.arithHilbertSamuel_of_ampleHS
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ArithHilbertSamuelNefOfAmple
covers: 346
status: drafted
drafted_by: writer@claude
---
This theorem is the last step of [the arithmetic Hilbert-Samuel formula from principalisation](/entry/arith-hilbert-samuel-of-principalisation/). It takes three statements that come from principalisation and gives $\mathrm{ArithHilbertSamuel}$ for nef hermitian line bundles. It reaches that entry through the restatement [`T.arithHilbertSamuel_nef_of_ample`](/entry/arith-hilbert-samuel-nef-of-ample/). The proof puts together a finiteness lemma, an upper bound and a lower bound. Those bounds have the real content.

## Statement

**Theorem.** $\mathrm{ArCalc}$, $\mathrm{AmpleHS}$ and $\mathrm{SemiPull}$ together imply $\mathrm{ArithHilbertSamuel}$.

The three hypotheses are described in [the parent entry](/entry/arith-hilbert-samuel-of-principalisation/): seven rules of arithmetic intersection numbers, the formula for ample bundles with a semipositive metric, and stability of semipositivity under pull-back. The conclusion is stated in [the literature entry](/entry/arith-hilbert-samuel-of-literature/). In short: let $X$ be an arithmetic variety of dimension $D+1$, let $\overline{L}$, $\overline{N}$ be hermitian line bundles on $X$, and let $\overline{L}$ be nef with arithmetic self-intersection $a$. Let $\widehat{H}^0_m$ be the set of small sections of $\overline{L}^m \otimes \overline{N}$. Then $\widehat{H}^0_m$ is finite for large $m$, and $\log \# \widehat{H}^0_m - a\, m^{D+1}/(D+1)! = o(m^{D+1})$.

## Proof

1. **Finiteness.** `T.finite_smallSec_hermitian_line_bundle_arith_variety` says that the set of small sections of each hermitian line bundle on an arithmetic variety is finite. So $\widehat{H}^0_m$ is finite for every $m$, not only for large $m$.
2. **Two bounds.** Fix $c > 0$. For all large $m$, $\bigl(a/(D+1)! - c\bigr) m^{D+1} \le \log \# \widehat{H}^0_m \le \bigl(a/(D+1)! + c\bigr) m^{D+1}$. The upper bound is `T.arith_nef_volume_upper_bound`, which uses all three hypotheses and that $\overline{L}$ is nef. The lower bound is `T.arithHilbertSamuel_lowerBound_semiPos_nefOnFibres`, which uses $\mathrm{ArCalc}$ and $\mathrm{AmpleHS}$. It needs only two parts of nefness: the metric is semipositive, and the degree on each vertical curve is nonnegative (`NefFib`, from `nefFib_of_isNef`).
3. Since $m^{D+1} \ge 0$, the two bounds give $\lvert \log \# \widehat{H}^0_m - a\, m^{D+1}/(D+1)! \rvert \le c\, m^{D+1}$. This is the definition of $o(m^{D+1})$. The rest is `linarith`.

## In the Lean code

The theorem is in [ArithHilbertSamuelNefOfAmple.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelNefOfAmple.lean#L16). The lemmas it calls:

- `T.finite_smallSec_hermitian_line_bundle_arith_variety`, a restatement of `SmallFin.smallSec_finite` in [FiniteSmallSecHermitianLineBundleArithVariety.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiniteSmallSecHermitianLineBundleArithVariety.lean#L15);
- `T.arith_nef_volume_upper_bound`, a restatement of `NefUpper.main` in [ArithNefVolumeUpperBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithNefVolumeUpperBound.lean#L36);
- `T.arithHilbertSamuel_lowerBound_semiPos_nefOnFibres`, a restatement of `HSNef.LowerNef.main` in [ArithHilbertSamuelLowerBoundSemiPosNefOnFibres.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelLowerBoundSemiPosNefOnFibres.lean#L25);
- `nefFib_of_isNef` in [NefFibOfIsNef.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NefFibOfIsNef.lean#L56), which takes the field `vertical` of `IsNef`.

We have not opened the proofs of the two bounds. The lower bound does not use the horizontal part of `IsNef` or `SemiPull`.
