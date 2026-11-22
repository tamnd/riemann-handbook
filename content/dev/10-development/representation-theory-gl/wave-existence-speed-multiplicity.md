---
id: wave-existence-speed-multiplicity
title: The wave equation on the complex general linear group, its kernels and multipliers
kind: theorem
decl: PositivityTheory.RgBcC.wave_existence_speed_multiplicity
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.ArchimedeanGelfandKernels.WaveFinal
covers: 1002
status: drafted
drafted_by: writer@claude
---
This theorem collects four facts about a wave equation on $\mathrm{GL}_n(\mathbb{C})$: solutions exist, they have finite propagation speed, kernels exist with compact support, and these kernels form an algebra of multipliers on joint eigenfunctions. It has 14 users and lies below [EveryCharacter from the Galois row](/step/every-character/). At the top level it only combines other lemmas.

## Statement

Let $G = \mathrm{GL}_n(\mathbb{C})$ and $K = \mathrm{U}(n)$. Let $\ell(y) = \log\bigl(1 + \sum_{a,b} |y_{ab}|^2 + |(y^{-1})_{ab}|^2\bigr)$. Let $(E, \rho)$ be a finite-dimensional unitary continuous representation of $K$. Let $C_E$ be the smooth $f \colon G \to E$ with $f(gk) = \rho(k)^{-1} f(g)$. For $X \in \mathfrak{gl}_n(\mathbb{C})$, let $R_X$ be the right derivative. Let $E_{ab} = \tfrac12(R_{e_{ab}} - i R_{i e_{ab}})$, let $\Gamma_m = \sum_a (E^m)_{aa}$, let $\bar\Gamma_m$ be the same with $+i$, and let $\Omega = 2(\Gamma_2 + \bar\Gamma_2)$.

A *wave* is a smooth $u \colon \mathbb{R} \times G \to E$ with $u(t, \cdot) \in C_E$, $\partial_t^2 u = \Omega u$ and $\partial_t u(0, \cdot) = 0$. A *kernel* for a word $w$ in the $\Gamma_m, \bar\Gamma_m$ and an even smooth $g$ with support in $[-T, T]$ is a smooth $k \colon G \to \mathrm{End}(E)$ with $\ell$-bounded support and $k(k_1 y k_2) = \rho(k_1) k(y) \rho(k_2)$ such that, for every wave $u$,
$$\int_G k(y)\, u(0, xy)\, dy = w\Bigl(\int_{\mathbb{R}} g(t)\, u(t, \cdot)\, dt\Bigr)(x).$$
A *multiplier* of radius $T$ is a finite sum $k = \sum c_i k_i$ of such kernels, with the value $\mathrm{val}(\chi) = \sum_i c_i\, w_i(\chi) \int g_i(t) \cosh\bigl(t\, \mathrm{cas}(\chi)^{1/2}\bigr)\, dt$. We have not fully unfolded `gelfVal`, which gives $w_i(\chi)$ and $\mathrm{cas}(\chi)$.

**Theorem.** For every $n$:

1. every $f \in C_E$ is $u(0, \cdot)$ for some wave $u$;
2. there is $c$, depending only on $n$, such that $u(t, x) = 0$ whenever $u(0, \cdot)$ vanishes on $\{xy : \ell(y) \le c(1 + |t|)\}$;
3. kernels exist for every $w$ and $g$, and there is $c$ with $k(y) = 0$ for every multiplier $k$ of radius $T \ge 0$ and $\ell(y) > c(1 + T)$;
4. multipliers are closed under convolution, with product values and added radii; they commute; $y \mapsto k(y^{-1})^*$ is a multiplier whose value is $\overline{\mathrm{val}}$ on Hermitian $\chi$ (`IsHerm`); and $k * f = \mathrm{val}(\chi) f$ for each $f \in C_E$ that is a joint eigenfunction of the $\Gamma_m, \bar\Gamma_m$ with parameter $\chi$.

## Proof

The proof takes six inputs: properties of $\ell$ (`LgFacts`), unimodularity of Haar measure (`Unimod`), a Sobolev inequality on $G$ (`SobG`), the calculus of right derivatives (`RCalc`), uniqueness of kernels (`KerUniq`) and an estimate in Lie algebras (`AlgEst`). From these, `finite_propagation_speed_holds` gives clause 2. Then `asmCpt` gives waves for compactly supported data, and `wave_solution_existence` gives clause 1. Next `asmKerOne` gives the first half of clause 3, and `wave_kernel_existence` gives clause 3. Last, `asmMult_main` gives clause 4.

## In the Lean code

The theorem is in [WaveFinal.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ArchimedeanGelfandKernels/WaveFinal.lean#L15). The four clauses are defined in [IsMultZero.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ArchimedeanGelfandKernels/IsMultZero.lean#L106), and the inputs in [WaveSt.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ArchimedeanGelfandKernels/WaveSt.lean#L24). The lemmas in the namespace `GlobalTheory.T` are one-line wrappers around lemmas in `CompanionTheory`, such as `WaveSpd.asmSpeed` and `WaveKer.asmKerEx`. We have not read those proofs.

The name is misleading: clause 4 (`MultAlg`) is about multipliers, not multiplicities. The first half of clause 3 (`KerEx`) repeats `KerOne` word for word, and `wave_kernel_existence` takes `KerOne` as a hypothesis, so that half only passes it along.
