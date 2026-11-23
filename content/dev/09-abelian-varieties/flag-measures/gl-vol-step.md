---
id: gl-vol-step
title: The volume of the space of lattices, from rank j - 1 to rank j
kind: theorem
decl: GlobalTheory.FlagBase.SiegelStep.glVol_step
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.GlNormOneAdelicQuotientVolumeSiegelStep
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem is the induction step for a volume $\mathrm{vol}_j(E)$ of lattices of rank $j$ over a totally complex field $E$. It expresses $\mathrm{vol}_j$ by $\mathrm{vol}_{j-1}$ and the Dedekind zeta value $\zeta_E(j)$. Two declarations use it: the restatement `T.glNormOneAdelicQuotientVolume_siegel_step`, and `glVol_lt_top`, which proves by induction that each $\mathrm{vol}_j$ is finite. In the dominator tree it sits directly below [EveryCharacter](/step/every-character/).

## Statement

Let $E$ be a totally complex number field with $f$ complex places $w$ and discriminant $d_E$. Put $v_E = |d_E|^{1/(2f)}/2$. Let $V_j = \prod_w \mathbb{C}^j$ with Lebesgue measure, and $M_j = \prod_w M_j(\mathbb{C})$. For $g \in M_j$ put $N(g) = \prod_w |\det g_w|^2$, and let $\mu_j$ be the Haar measure $N(g)^{-j}\,dg$. An $\mathcal{O}_E$-lattice $\Lambda \subset E^j$ has the group $\mathrm{Aut}(\Lambda) = \{\gamma \in \mathrm{GL}_j(E) : \gamma\Lambda = \Lambda\}$, embedded in $M_j$ by the places. Define

$$\mathrm{vol}_j(E) = \sum_{[\Lambda]} \mathrm{covol}_{\mu_j}\bigl(\mathrm{Aut}(\Lambda),\ \{g : 1 \le N(g) < e\}\bigr) \in [0, \infty],$$

with the sum over the classes of lattices under $\mathrm{GL}_j(E)$. Here $\mathrm{covol}(\Gamma, A)$ is the infimum of $\mu_j(D)$ over measurable sets $D$ that meet the $\Gamma$-orbit of each point of $A$.

**Theorem.** Let $j \ge 2$ and suppose $\mathrm{vol}_{j-1}(E) < \infty$. Then

$$\mathrm{vol}_j(E) = \mathrm{vol}_{j-1}(E)\cdot v_E^{\,f(2j-1)}\,\zeta_E(j).$$

With `glVol_one`, which gives $\mathrm{vol}_1(E) = \operatorname{Res}_{s=1}\zeta_E(s)\, v_E^{f}$, induction gives $\mathrm{vol}_j(E) = \operatorname{Res}_{s=1}\zeta_E(s)\, v_E^{fj^2} \prod_{l=2}^{j} \zeta_E(l)$.

## Proof

For $g \in M_j$ with $N(g) > 0$ let $L_g = g^{-1}\Lambda \subset V_j$, with covolume $c(L_g)$ and dual $L_g^*$ for the form $\operatorname{Re}\sum_w x_w \cdot y_w$. For a function $F$ of lattices, the mean $\mathcal{M}(F)$ sums over the classes $[\Lambda]$ the integral of $F(L_g)$ over a fundamental domain of $\mathrm{Aut}(\Lambda)$. Let $\Phi(x) = e^{-\pi\|x\|^2}$, so $\int \Phi = 1$, and put $C_j = \mathrm{vol}_{j-1} v_E^{f(2j-1)} \zeta_E(j)$.

1. Poisson summation (`T.poisson_summation_infinitePlaceGaussian_lattice`) gives $1 + A = c^{-1}(1 + B)$, with $A = \sum_{L \setminus 0} \Phi$, $B = \sum_{L^* \setminus 0} \Phi$ and $c = c(L)$. Then the lemma `weighted` gives
$$\mathbf{1}_{c>1}(c^{-1} - c^{-2}) + \mathbf{1}_{c>1}\, c^{-1} A = \mathbf{1}_{c^{-1}<1}\, c^{-2} B.$$
2. Take the mean of both sides. By `latMean_add` the mean of the left side is the sum of two means.
3. `T.lineLatticeClassMean_covolume_function` gives $\mathcal{M}(w(c(L))) = \mathrm{vol}_j \int_0^\infty w(t)\,dt/t$. The first mean is $\mathrm{vol}_j \int_1^\infty (t^{-2} - t^{-3})\,dt = \mathrm{vol}_j/2$.
4. `T.lineLatticeClassMean_sum_nonzero_unfold` gives $\mathcal{M}\bigl(w(c(L)) \sum_{L\setminus 0}\Phi\bigr) = C_j \int\Phi \int_0^\infty w(t)\,dt/t^2$. The second mean is $C_j/2$.
5. `T.translatedLatticeAtInfinity_full_covolume_dual` gives $c(L^*) = c(L)^{-1}$ and $L^{**} = L$. `T.lineLatticeClassMean_traceFormDualLattice` says that $\mathcal{M}(F(L^*)) = \mathcal{M}(F(L))$. So the mean of the right side is $\mathcal{M}\bigl(\mathbf{1}_{c<1} c^2 \sum_{L\setminus 0}\Phi\bigr) = C_j \int_0^1 dt = C_j$.
6. Hence $\mathrm{vol}_j/2 + C_j/2 = C_j$. Since $C_j < \infty$, $\mathrm{vol}_j = C_j$.

The argument has the shape of Siegel's mean value method for lattices. We do not know a published source for this form over a totally complex field.

## In the Lean code

The theorem is in [GlNormOneAdelicQuotientVolumeSiegelStep.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/GlNormOneAdelicQuotientVolumeSiegelStep.lean#L214). The definitions `glVol`, `haarGL`, `detNorm`, `autGL` and `covol` are in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L104); `latAt`, `dualAt`, `latMean`, `covAt` and `gaussV` are in [IsLatMeasurableConst.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsLatMeasurableConst.lean#L50). The constant $v_E$ is `vInv` and $f$ is `fDeg`.

- The three mean value formulas and the lattice facts are restatements whose proofs we have not read: `MeanCov.latMean_covAt`, `SiegelUnfold.latMean_sum_ne_zero`, `MeanDual.latMean_dualAt` and `LatFacts.lattice_facts`.
- The four integrals are `lintegral_diff`, `lintegral_cube`, `lintegral_unit` and `lintegral_gauss` in the same file.

The hypothesis $\mathrm{vol}_{j-1} < \infty$ is needed only to cancel $C_j/2$ in the last step. The module name speaks of an adelic norm-one quotient. The Lean object is a sum of archimedean covolumes over classes of lattices, on the slab $1 \le N(g) < e$; we have not checked that the two agree.
