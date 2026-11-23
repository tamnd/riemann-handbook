---
id: lift-f-of-is-good
title: Lifting crystalline classes along a surjection of good lattices
kind: theorem
decl: GlobalTheory.TheoremT.liftF_of_isGood
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftSurjectionGoodCrystallineLattices
covers: 2788
status: drafted
drafted_by: writer@claude
---
This theorem is the core of the local lifting statement `thmT`. For a surjection $g \colon T_1 \to T_2$ of good lattices, it bounds the cokernel of the map on lattice crystalline cohomology by an explicit power of $\ell$. It goes through Breuil-Kisin modules with tame descent data. Its wrapper [`lift_surjection_good_crystalline_lattices`](/entry/lift-surjection-good-crystalline-lattices/) is used in step 5 of [`TheoremTClosing.main`](/entry/theorem-tclosing-main/).

## Statement

The notation is that of [`TheoremTClosing.main`](/entry/theorem-tclosing-main/): lattices $T$ of $G = G_{\mathbb{Q}_\ell}$ over $\mathcal{O}_L$, crystalline cocycles $Z^1_f(T)$, coboundaries $B^1(T)$. Let $a, e \ge 1$ with $e + 1 = \ell^a$ and $\ell \nmid a$. Let $L$ contain the unramified extension of degree $a$ and a primitive $e$-th root of unity. Let $\varpi$ be a system of roots with $\varpi_0^e = -\ell$ and $\varpi_{n+1}^\ell = \varpi_n$, and let $K_\varpi$ be the unramified extension of degree $a$ with $\varpi_0$ adjoined. The period rings are standard (`IsStd`, which we did not unfold).

For $\Sigma \subset \mathbb{Z}/e$ and $U \subset \mathbb{Z}$ finite, a lattice $T$ is *good* (`IsGood`) if:

1. the restriction of $V$ to $G_{K_\varpi}$ is crystalline;
2. (tame type) for each $\sigma$ in the inertia group of $\mathbb{Q}_\ell$, with $w = \sigma(\varpi_0)/\varpi_0$, the operator $\prod_{c \in \Sigma} (\sigma - w^c)$ kills $D_{\mathrm{cris}}$ of the restriction;
3. the Hodge-Tate jumps of $V$ at each embedding lie in $U$.

`Numerics` asks: $\ell c \in \Sigma$ for $c \in \Sigma$, $0 \in \Sigma$, $|\Sigma| \le N$, $N \ge 2$, $U \subset [-\eta, H]$, $0 \in U$, $|U| \le N + 1$, $1 \le \eta < H$ and $40(HN^2 + N^3) < \ell$. Let $r$ be the largest, over $c, c' \in \Sigma$, of the period of $c - c'$ under $x \mapsto \ell x$ (`maxPeriod`).

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `FontaineBcris`. Under `Numerics`, let $g \colon T_1 \to T_2$ be a map of lattices onto $T_2$, with $T_1, T_2$ good for $(\Sigma, U)$. Then

$$\ell^{\,7(Nr + \eta(N + r))} Z^1_f(T_2) \subset g_* Z^1_f(T_1) + B^1(T_2).$$

## Proof

Write $\varepsilon = 2(N-1)r$ (`eW`), $c_1 = \eta(r+1)$ (`cOne`) and $k$ for `kExp N η r`. From $N \ge 2$ and $40(HN^2 + N^3) < \ell$ we get $\ell \ne 2$ and $8H + 1 < \ell$.

1. **The kernel.** `isGoodLattice_kernel_of_surjection_goodLattice` gives a good lattice $T_0$ and a short exact sequence $0 \to T_0 \to T_1 \to T_2 \to 0$.
2. **Breuil-Kisin modules.** [`exists_breuilKisinModule_tameDescent_goodLattice`](/entry/exists-breuil-kisin-module-tame-descent-good-lattice/) gives a Breuil-Kisin module with tame descent datum $P_i$ for each $T_i$, of type $(\Sigma, U)$. `latticeHom_lifts_breuilKisinDescentHom` lifts $f$ and $g$ to maps $F \colon P_0 \to P_1$ and $G \colon P_1 \to P_2$. `isExactTriple_breuilKisin_of_shortExactLattices` says that $P_0 \to P_1 \to P_2$ is exact.
3. **A module element for $c$.** Let $c \in Z^1_f(T_2)$. `crystalline_class_from_monodromy_kernel_element` gives $y_2$ in $P_2$ with monodromy $0$ whose Galois class is $\ell^{\varepsilon} c$. `prime_pow_divisibility_of_descentDatum` writes $\ell^\eta y_2 = y_2' + (\varphi(m_2) - m_2)$. The rules for classes in `exists_frobeniusPotential_cocycle_class` show that $y_2' + \varphi(m_2)$ has monodromy $0$ and class $\ell^{\eta + \varepsilon} c$.
4. **Lift to $P_1$.** `liftingTheorem_phiModules_exact_triple` (the statement `Lifting`) gives $y', m$ in $P_1$ with monodromy of $y' + \varphi(m)$ equal to $0$ and $G(y' + \varphi(m)) = \ell^{k}(y_2' + \varphi(m_2))$.
5. **Back to Galois.** `zeta_mem_pow_inv_phiModule_lattice` makes $\ell^{c_1}\zeta(y' + \varphi(m))$ integral. Then `galoisClass_of_monodromy_eq_zero` gives $\kappa_1 \in Z^1_f(T_1)$, a class of $\ell^{c_1}(y' + \varphi(m))$.
6. **Compare.** By naturality (`tame_breuil_kisin_datum_exists`), $g_*\kappa_1$ is a class of $\ell^{c_1 + k}(y_2' + \varphi(m_2))$. By step 3, so is $\ell^{s} c$ with $s = c_1 + k + \eta + \varepsilon$. Two classes of one element differ by an element $\beta \in B^1(T_2)$. So $\ell^{s} c = g_*\kappa_1 - \beta$.
7. **Exponent.** $s = 2\eta r + (N + 5)\eta + 6(N - 1)r \le 7(Nr + \eta(N + r))$ for $N \ge 2$ (by `nlinarith`). Multiply by the remaining power of $\ell$.

## In the Lean code

The theorem is in [LiftSurjectionGoodCrystallineLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftSurjectionGoodCrystallineLattices.lean#L27). `IsGood` and `TameType` are in [IsPotential.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotential.lean#L117), and `Numerics` and the exponents in [ConductorExponents.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/ConductorExponents.lean#L20). Each lemma of the proof above is a "Statement" wrapper of a lemma in another file. We did not open those proofs, nor the definitions of monodromy, $\zeta$ and Galois classes in the Breuil-Kisin data.

Odd points:

- `Numerics` and `Admissible` ([AdmissibleSignatures.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/AdmissibleSignatures.lean#L10)) are two structures with the same ten fields. Lines 45 to 47 copy one into the other.
- $H$ does not appear in the exponent. It enters through $8H + 1 < \ell$ in step 5.
- The type of $P_0$ is discarded (line 38); only its existence is used.
