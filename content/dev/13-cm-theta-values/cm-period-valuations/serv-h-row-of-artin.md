---
id: serv-h-row-of-artin
title: The service row from Artin reciprocity
kind: theorem
decl: GlobalTheory.Svd.servH_row_of_artin
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.BundleBothPartsOfStandardKernelOfGlobalArtinReci
covers: 10811
status: drafted
drafted_by: writer@claude
---
This theorem proves the service row `ServH` for any slot of points, linkage of bundles and kernel map, from global Artin reciprocity and two side conditions. Artin reciprocity gives one statement about [[elliptic curves|427N6S6QQW]] with complex multiplication, and from it the proof gets the six hypotheses of [`servH_row`](/entry/serv-h-row/). Its user is the renaming [`bundle_bothParts_of_standardKernel_of_globalArtinReciprocity`](/entry/bundle-both-parts-of-standard-kernel-of-global-artin-reciprocity/), and through it [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/), which gives the field `hServ` of `AllRowsAlt` in [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

- A *slot* $Q$ is a predicate on constructed cores. A *constructed point* $\beta$ (`BPt K`) is a core with a layer, a part of it and fourteen conditions that tie them to the context $K$. A *linkage* $L_k$ is a predicate on bundles $b$ at constructed points. The map `ker` sends each bundle to a tied kernel entry.
- `RowE Q Lk E`: for all small $\varepsilon$ and all large constants, there is $x_0$ such that, at each context of scale $x \ge x_0$, every bundle at a point of $Q$ that $L_k$ links satisfies $E$.
- `Row Q Lk H`: there is $E$ with `RowE Q Lk E` such that $H(\mathcal A, \sigma)$ holds for every class $\mathcal A$ of families and every selection $\sigma$ along $E$. Such a selection picks, for each family in $\mathcal A$, each large $x$ and each index $i$, a bundle that comes from a point of $Q$, is linked by $L_k$ and satisfies $E$.
- `ServH ker 𝒜 σ` has two parts. First, `Closed 𝒜 RowTwU`: each large family in $\mathcal A$ satisfies the twisted row condition `RowTwU`, in the sense of `Closed` of [the chapter](/proof/unitary-hypotheses/). Second, the kernel entry of each selected bundle satisfies `Pdv.At`, a list of named conditions (an orbit bound, jet integrality, a theta kernel shape and others). We have not unfolded them.

**Theorem.** Assume `GlobalArtinReciprocity` (stated in [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/)). Suppose that each point of $Q$ is in `positionOf HasPart` (its core comes from a column at which a `Part` exists), and that `RowE` holds for the property "`ker b` has a standard tie" (`StdTie`). Then `Row Q Lk (ServH ker)`.

## Proof

1. `cmGoodModel_of_globalArtinReciprocity` gives `CM2`. This says: let $d$ be squarefree with $d \equiv 3 \pmod 4$, and let $L \subset \mathbb C$ be a lattice with $\omega L \subseteq L$ for $\omega = (1 + \sqrt{-d})/2$. Let $\ell \ge 5$ be a prime with $\ell \nmid d$ and $\iota \colon \mathbb C \to \mathbb C_\ell$ a field isomorphism. Then there are $g_2, g_3$ in the closure of the maximal unramified extension of $\mathbb Q_\ell$, with $|g_2|, |g_3| \le 1$, $|g_2^3 - 27 g_3^2| = 1$, and $g_2 = \lambda^4 \iota(g_2(L))$, $g_3 = \lambda^6 \iota(g_3(L))$ for some $\lambda \ne 0$. Inside, `exists_idealClass_artinSymbol_of_globalArtin` gives a map from the Galois group to the class group that kills inertia and sends a Frobenius at $v$ to the class of $v$, and `cmLattice_good_model_unramified` (not read by us) turns it into `CM2`.
2. `torsionTaylorAlgebraic_latticeExists_of_cm` gives `AlgTAll`, `GenusOneModelExistsLattice` and `CurveDict`. `intInert_of_complexMultiplication_condition` gives `IntInert`. [`inert_theta_admissibility_of_complex_multiplication`](/entry/inert-theta-admissibility-of-complex-multiplication/) (1,230 declarations) gives `AdmAtEnt2`. `exists_genusOne_formal_iso_of_unramified_good_reduction` gives `CurveEx`.
3. Apply [`bundle_bothParts_of_standardKernel_and_six_hypotheses`](/entry/bundle-both-parts-of-standard-kernel-and-six-hypotheses/) (5,806 declarations).

## In the Lean code

The theorem is at [BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean#L15). `ServH` is at [HasPartAnd.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L45), `RowE` and `Row` at [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L261), and `CM2` at [Statement.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/CMGoodModels/Statement.lean#L45).

Artin reciprocity is used only to get `CM2`, and the side conditions are passed along. `AlgTAll` does not need `CM2`: it is the theorem `algTAll`. The proofs of `IntInert` and `AdmAtEnt2` install `CM2` as an instance (`Fact CM2`) and apply a lemma stated under `variable [Fact CM2] in`.
