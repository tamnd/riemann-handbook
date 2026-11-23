---
id: cls-kl-is
title: The kernel class datum of a pinned column is good
kind: theorem
decl: GlobalTheory.KerLaws.clsKL_is
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.KernelPartLawsOfColumnPins
covers: 345
status: drafted
drafted_by: writer@claude
---
This theorem proves the five conditions of a kernel class datum for the datum `clsKL` that a pinned column gives. Its only user is the second name [`kernelPart_laws_of_columnPins`](/entry/kernel-part-laws-of-column-pins/), which is step 3 of [class data from the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/). The proof gets each condition from one or two lemmas.

## Statement

Use the notation of [class data from the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/): a real datum $\rho$ = `realOf u R g s J` with ranks $N_j$, dominant weights $\lambda_j$ and real points $k \mapsto \rho.r_j(k)$, and a tuple $t$ built from a row choice $r$ and a column choice $k$. Let $A$ be a twist datum (`TwDat`): for each $j$ and each character $\alpha$, a subgroup $U_j(\alpha)$, a character $\chi_j(\alpha)$ of it, and representatives $h_j(\alpha, a)$ for the classes $a$ over $\alpha$. From $A$ come linear forms $\mathrm{ab}_j$ (`TwDat.abelian₂`). Let $\iota_j$ map the column characters into the characters of $A$.

The datum `clsKL` takes, at $(j, \beta)$, the classes of $A$ over $\iota_j(\beta)$, with $U$, $\chi$, $h$ and $\mathrm{ab}$ from $A$, and the value of $\psi$ at a class $a$ is $\psi(a)$.

`ClsK.Is` has five parts:

1. `Forms`: $U$ is compact open in the finite adelic group, and the $h(a)$ are finite adelic representatives of the double cosets $G(\mathbb{Q}) \backslash G(\mathbb{A}) / G_\infty U$, each met once; each $\chi$ is continuous; the values lie in the space of $\lambda_j$; and the reading of a ramified $\psi$ at $\gamma\, h(a)\, k\, \kappa$ is $\chi(\kappa)$ times the value at the moved point;
2. `Real`: the kernel at real points $(k, k')$ is the kernel at moved points times $\prod_\tau \det \rho.r_j(k)_\tau^{s_S} \det \rho.r_{j+1}(k')_\tau^{-s_D}$;
3. `Lev`: $(\kappa, \kappa') \in U_j(\alpha) \times U_{j+1}(\gamma)$ acts on the vacuum combination by $\chi_j(\kappa)^{-1} \chi_{j+1}(\kappa')$;
4. `Core`: $\mathrm{vol}(U_j(\alpha))$ times the theta integral at two representatives is $c_K(j)$ times $\mathrm{ab}_j$ at a scaled polynomial;
5. `Kval`: the values at $j + 1$ of $K_j \psi$ (`t.K j ψ`) are a sum over classes at $j$ of $\mathrm{ab}_j$ applied to restrictions, with weights $1/|\mathrm{Stab}|$.

**Theorem.** Assume `I.Ok`, `TC.Pins`, `PinX` for $g$ and $c_0$, `JetS` for $s$, that each $g.x_j$ ($j \le m$) satisfies `Is`, and `PinChL R g k c₀ A ι w`. Then `clsKL` satisfies `ClsK.Is`.

## Proof

Each part comes from one or two lemmas.

- `Forms`: `chartLevels_reps_represent_unitaryDoubleCosets` gives the representatives and the continuity. `scalarForms_on_charts_of_trueColumnTuple` gives the values and the reading, with the field `rdq` of `PinChL` to match the readings.
- `Real`: `livechart_kernelVectors_realPoints_detPowers`.
- `Lev`: `chartLevelPair_action_finiteDatum_law`.
- `Core`: `thetaKernelIdentity_at_every_tuple`, with $s_j \neq 0$ and the jet identity from `JetS`.
- `Kval`: `liveCharts_kernel_eq_classSum_jets`.

The rest is unfolding `clsKL`, `realOf` and `tupOf` with `simp`.

## In the Lean code

The theorem is at [KernelPartLawsOfColumnPins.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/KernelPartLawsOfColumnPins.lean#L22). `ClsK` and `ClsK.Is` are in [OnFramesRdApply.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/OnFramesRdApply.lean#L69), and `clsKL` and `PinChL` in [PinColL.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PinColL.lean#L49). The six lemmas are restatements in `*Statement.lean` files of this folder. We have not opened their proofs, and we have not unfolded `PinX`, or `JetS` beyond its two parts.

Of `PinChL` the proof uses `is`, `ram` and `rdq` directly, and passes the whole hypothesis to the lemmas. The hypothesis on $g.x_j$ is used only by the lemmas for `Real` and `Kval`.
