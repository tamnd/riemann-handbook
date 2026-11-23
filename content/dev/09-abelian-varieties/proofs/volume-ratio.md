---
id: volume-ratio
title: The volume ratio of hermitian spaces, from the one-vector Siegel-Weil formula
kind: theorem
decl: GlobalTheory.VolRatioFromSecondClause.volumeRatio
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.VolumeRatio
covers: 534
status: drafted
drafted_by: writer@claude
---
This theorem computes the ratio of the volumes of two hermitian spaces whose ranks differ by one. It has one hypothesis, a one-vector form of the Siegel-Weil formula. Its result is the field `hU` of the record [HypsAlt](/step/hyps-alt-def/), which feeds the [literature step](/step/every-character-of-literature/). It has two callers: `GlobalTheory.VolRatioFromSiegelWeil.volumeRatio` supplies the hypothesis from `SiegelWeilUnitaryConvergent`, and `CompanionTheory.HU.hU_of` takes it as `SiegelOneAll`.

## Statement

Let $\mathrm{SW}_1$ be the following statement (`SW1b2`). Let $E/F$ be a CM extension with complex conjugation $\sigma$, and let $J$ be a nondegenerate hermitian $M \times M$ matrix over $E$, with unitary group $H = U(J)$. Suppose $M \geq 3$ and $\beta \in F^\times$. Let $\Phi = \Phi_\infty \cdot \Phi_f$ be a nonnegative test function on $(\mathbb{A}_F \otimes_F E)^M$, with $\Phi_\infty$ measurable and $\Phi_f$ a pure tensor $\bigotimes_v \Phi_v$ of real nonnegative local factors. Fix a character $\psi$ of $\mathbb{A}_F / F$ (the predicate `IsCharAF`, which we did not unfold), a Haar measure $\mu$ on $H(\mathbb{A}_F)$, a fundamental domain $\mathcal F$ for $H(F)$, and self-dual measures at each place. Then the fibre measures $\mu_{\infty,\beta}$ and $\mu_{v,\beta}$ on the local quadrics $\{h(x,x) = \beta\}$ exist, their product converges, and

$$\frac{1}{\mu(\mathcal F)} \int_{\mathcal F} \sum_{\substack{0 \neq x \in E^M \\ h(x,x) = \beta}} \Phi(h^{-1}x)\, d\mu(h) = \int \Phi_\infty\, d\mu_{\infty,\beta} \cdot \prod_v \int \Phi_v\, d\mu_{v,\beta}.$$

The code names this a clause of the Siegel-Weil formula. We have not compared its normalizations with those of Weil (Acta Math. 113, 1965).

**Theorem.** Assume $\mathrm{SW}_1$ for all CM extensions and all $J$. Let $D$ be a datum of type `D7`, with CM field $E$ and volume function $\mathrm{vol}$ on hermitian spaces over $E$. Suppose that $\mathrm{vol}(W)$ is the Haar volume of a fundamental domain, with the measure normalized at the self-dual lattice (`VolTie`). Let $W$ have rank $M \geq 3$ and the same signature $(P, Q)$ at every real place. Let $s = \pm 1$, with $P \geq 1$ if $s = 1$ and $Q \geq 1$ if $s = -1$. Then there are $x \in W$ with $h(x,x) = s$ and a hermitian space $W' \cong x^\perp$ of signature $(P-1, Q)$ or $(P, Q-1)$, with

$$\frac{\mathrm{vol}(W')}{\mathrm{vol}(W)} = \left(\frac{(2\pi)^M}{(M-1)!}\right)^{f} \frac{(2v)^{f(1/2 - M)}}{L_\eta(M)}.$$

Here $f$ is the integer `D.R.f`, $v = |d_E|^{1/[E:\mathbb{Q}]}/2$, and $L_\eta(M)$ is the Euler product `lValEta E M`. Its factor is $(1 - q^{-M})^{-1}$ at a split place of norm $q$ and $(1 - (-q)^{-M})^{-1}$ at an inert one.

## Proof

The proof applies `volumeRatio_of_unfolding` to six proved lemmas and to the hypothesis. Inside it, `unitVectorPerp` finds $x$ in a self-dual lattice $L$ with $L = \mathcal O_E x \oplus (L \cap x^\perp)$. `volIndep` shows that $\mathrm{vol}(W)$ does not change when the lattice of $W$ is replaced by $L$. Then `ratio_of_setting` applies $\mathrm{SW}_1$ with $\beta = s$ and the test function of $L$. `unfolding` turns the left side into $\mathrm{vol}(W')$ times an orbit integral. `realPlaceMeasures` computes the factor at infinity, and `selfDualLatticeDensity` with `eulerProductOfDensities` give $L_\eta(M)$. We have not followed `ratio_of_setting` line by line.

## In the Lean code

The theorem is in [VolumeRatio.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/VolumeRatio.lean#L14). The work is in [VolumeRatioOfUnfolding.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/VolumeRatioOfUnfolding.lean#L393). The lemmas it passes are `selfDualLatticeDensity`, `realPlaceMeasures`, `eulerProductOfDensities`, `volIndep`, `unitVectorPerp` and `unfolding`. The hypothesis $\mathrm{SW}_1$ is [`SW1b2`](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLattice.lean#L75), and the conclusion `MassRatioUnderVolume D` is [`VolTie D → VolumeRatio₂ D`](lean:Formalism/SharpRestriction/GlobalSchurBounds/MassRatioUnfoldedOfTheoremTwo.lean#L12).

The quantifier on $\psi$ is `AllSome`: some character exists, and the formula holds for all of them.
