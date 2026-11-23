---
id: ad-law-at-xi-ad
title: The adelic datum of a kernel chain and its laws
kind: theorem
decl: GlobalTheory.TwV.adLawAt_xiAd
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.AdelicChainDatumCharacterLawsJointKernel
covers: 710
status: drafted
drafted_by: writer@claude
---
This theorem proves that an explicit adelic datum $\Xi$ and characters $\mu_T$ satisfy the thirteen laws of `AdLawAt`. Through [`adelicChainDatum_characterLaws_jointKernel`](/entry/adelic-chain-datum-character-laws-joint-kernel/) and [`exists_adLawAt_joint`](/entry/exists-ad-law-at-joint/), these become the fields `Xi`, `muT` and `law` of the joint site that [`joint_at_nonempty`](/entry/joint-at-nonempty/) builds. Twelve called lemmas give eleven laws; `read` and `mu_cls` are proved here.

## Statement

Fix a tied kernel entry $t$, a word $u$ and a tuple $\mu$. There are $m = m_2 + 2$ steps, with Hermitian Gram matrices $J_i$. Let $\mathrm{St}$ be chain charts: at each step $i$ a set of charts $\beta$, a level group $K_\beta$ with a character $\chi_\beta$, and a point $y_c$ of $U(J_i)(\mathbb{A}_{F,f})$ for each class $c$. Let $A$ be adelic data (`AdData`), with coordinate matrices $\mathrm{crd}_i \in \mathrm{GL}_{N_i}(E)$ and chain points $A.\mathrm{pt}_i(c)$. Let $d_U$ be a homomorphism from the norm-one finite ideles $U^1$ to `D.Dt`, and $a \in \mathcal{O}_E$.

The datum $\Xi = $ `xiAd A a`: let $x \in U(J_i)(\mathbb{A}_{F,f})$ and $x' \in U(J_{i+1})(\mathbb{A}_{F,f})$. If both have chain points $q$, $q'$ (`IsPtAd`), then $\Xi_i(\beta, \beta', x, x')(z) = \sigma_0(\xi_i(q, q', z'))$, where $z'$ is $z$ in the coordinates $\mathrm{crd}$, and $\xi_i$ (`xiPt`) is the kernel entry value: `XiEntry` for $i < m_2$, `XiCpl1` for $i = m_2$, `XiTop` for $i = m_2 + 1$. Otherwise $\Xi$ is $0$. The characters are $\mu_T(j)(x) = \mathrm{mt}_j(d_U(y))$ for a chosen $y \in U^1$ with $x = \det y$, and $0$ if there is none.

**Theorem.** If `AdPins A dtU` and `AdTie A dtU a` hold, then `AdLawAt A dtU a Ξ μ_T` holds. Its fields say:

- `read`: at the class points $y_c, y_{c'}$, $\Xi$ is the datum $\Xi^{\mathrm{rd}}_i(c, c')$ of the kernel record, in the coordinates $\mathrm{crd}$;
- `rat`, `lev`, `away`: $\Xi$ is invariant under rational unitary $\gamma$ on the left, changes by $\chi_\beta$ and $\mu_T(\det)$ under the level groups on the right, and depends only on the components of $x, x'$ under the bad set $SS$;
- `loc`, `supp`, `int`: $\Xi$ is locally constant at $SS$, supported on a lattice, and algebraic and $p$-integral for $p$ outside a finite set;
- the six `mu_` fields: $\mu_T(i+1)$ is $\mathrm{mt}_{i+1} \circ d_U$ on determinants of $U^1$ and of class points, multiplicative on $U^1$, algebraic, trivial on integral units that are $1$ above the selected primes, and equal to $\prod_\tau \tau(z)^{e_\tau}$ on rational $z$ with $z \bar z = 1$.

## Proof

1. `chartPoints_exist_and_classPoints_representatives`: every $x$ has a chain point; $A.\mathrm{pt}_i(c)$ is one for $y_c$.
2. `stepCharacterLaws_normOneIdeles_of_kernelChain` gives the `mu_` fields other than `mu_cls`.
3. `PtAway`, in the cases $i < m_2$, $i = m_2$, $i = m_2 + 1$: `finiteDatum_dependsOnlyAtBadPlaces_matrixStep`, `…_firstCoupledStep`, `ptAway_top`. So the choice of chain points does not matter, and `away` holds.
4. `lev`, in the same cases: `finiteDatum_levelEquivariance_at_matrixSteps`, `adelicDatum_level_equivariance_first_coupled_step`, `lastStep_adelicDatum_level_equivariance`.
5. `finiteAdelicDatum_rationalInvariance_of_kernelChain` gives `rat`; `adelicDatum_invariance_support_kernelChain` gives `loc` and `supp`; `adelicFiniteDatum_integralOffBadPrimes` gives `int`.
6. `read`: by step 3, $\Xi$ at class points is $\sigma_0 \xi_i$ at $A.\mathrm{pt}$, and the chain condition of `AdTie`, with `couplingCoset_eq_chartPointCoset` at $i \ge m_2$, gives $\xi_i = \Xi^{\mathrm{rd}}_i$.
7. `mu_cls`: `exists_u1Af_det` writes $\det y_c = \det y$ with $y \in U^1$; then `mu_read` and `AdTie.dt` apply.

## In the Lean code

The theorem is at [AdelicChainDatumCharacterLawsJointKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L62). `xiAd` and `muOf` are in [UnderTie.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/UnderTie.lean#L48), `AdData`, `AdPins`, `AdTie` and `AdLawAt` in [ExistsMidLevIff.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ExistsMidLevIff.lean#L584). The helpers `xiAd_eq_of_isPtAd` and `exists_u1Af_det` are in the same file. We have not unfolded `XiEntry`, `XiCpl1`, `XiTop`, `IsChainTopW` or `DatLoc`.

Both $\Xi$ and $\mu_T$ use `Classical.choose` and take the value $0$ off their natural domain.
