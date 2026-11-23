---
id: class-of-of-mon-eq-zero
title: A Breuil-Kisin element with zero monodromy gives a crystalline class
kind: theorem
decl: GlobalTheory.BKGal.classOf_of_mon_eq_zero
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.GaloisClassOfMonodromyEqZero
covers: 316
status: drafted
drafted_by: writer@claude
---
This theorem turns an element $y$ of a Breuil-Kisin pack with zero monodromy into a crystalline cocycle of the Galois lattice, after multiplication by a power of $\ell$. It is the proof behind the second name [`galoisClass_of_monodromy_eq_zero`](/entry/galois-class-of-monodromy-eq-zero/), which step 5 of [`liftF_of_isGood`](/entry/lift-f-of-is-good/) uses to go back from Breuil-Kisin modules to Galois cohomology.

## Statement

Let $D$ be a pack datum `BKDat` with heights $(\eta, H)$ and $R$ a datum `GalDat` that ties it to a lattice $T$ of $G_{\mathbb{Q}_\ell}$, as in [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/). The notation for $M$, $S\varphi^*M$, $E$, $N = X\nabla$ and $M_R$ is that of [`ENStable_and_jumps`](/entry/enstable-and-jumps/).

- $Y$ (`D.Y`) is the set of $y$ with $E^\eta y \in M$ that the descent datum fixes.
- $\zeta(y) = -\sum_{j \ge 1} (\ell\varphi)^j N y$ (`zeta`).
- The *monodromy* of $y$ (`Mon`) is the class of $E N y - E\zeta(y)$ modulo $M_R$.
- A *potential* of $y$ (`IsPotential`) is $b = j_B(\sigma) - b_0$ in $B \otimes T$. Here $\varphi(m_0) - m_0 = y$ over Witt vectors, $b_0$ is the crystalline value of $\varphi(m_0)$, and $\sigma$ is fixed by the descent datum with $N\sigma = \zeta(y)$.
- A cocycle $\kappa$ is a *class of* $y$ (`ClassOf`) if $\kappa(g) = g b - b$ for a potential $b$ of $y$.
- $Z^1_f(T)$ (`latticeFiniteCocycles`) is the set of continuous cocycles with values in $T$ that are coboundaries in $V \otimes B$.

**Theorem.** Assume `FontaineBcris` and standard period data. Let $\eta < H$ and $8H + 1 < \ell$. Let $y \in Y$ with monodromy $0$, and let $c \ge 0$ with $\ell^c \zeta(y) \in S\varphi^*M$. Then some $\kappa_1 \in Z^1_f(T)$ is a class of $\ell^c y$.

## Proof

1. `exists_frobeniusPotential_cocycle_class` gives a potential $b$ of $y$.
2. `galois_eq_mul_kisinInf_tameSemidirect` writes each $g \in G_{\mathbb{Q}_\ell}$ as $g = hk$, with $h \in G_{K_\varpi}$ and $k$ in the Galois group of the Kummer tower $\mathbb{Q}_\ell(\varpi_n^e : n \ge 0)$.
3. For $k$: `cocycle_mem_lattice_on_kummerTowerGalois` gives $kb - b \in T$.
4. For $h$: `galois_coboundary_mem_lattice_inv_l_of_monodromy_eq_zero` uses the zero monodromy and `FontaineBcris` to get $\ell^n(hb - b) \in T$ for some $n$. `potentialCocycle_mem_lPow_lattice` lowers $n$ to $c$, with $\ell^c\zeta(y) \in S\varphi^*M$, $\eta < H$ and $8H + 1 < \ell$.
5. From $gb - b = h(kb - b) + (hb - b)$ we get $\ell^c(gb - b) \in T$. So $\kappa(g) = gb - b$ is a class of $y$ with $\ell^c\kappa$ in $T$.
6. `coboundary_mem_cocycles_odd_prime` ($\ell \ne 2$) makes $\kappa$ a continuous cocycle. `exists_bcrisTensorLattice_equiv_periodRing` shows that it is crystalline, since it is a coboundary in $B \otimes T$.
7. Put $\kappa_1 = \ell^c\kappa$. It lies in $Z^1_f(T)$, and part 3 of `exists_frobeniusPotential_cocycle_class` makes it a class of $\ell^c y$.

## In the Lean code

The theorem is in [GaloisClassOfMonodromyEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GaloisClassOfMonodromyEqZero.lean#L102), with steps 2 to 5 in the helper lemmas `step_mul`, `cob_of` and `exists_cob` of the same file. `IsPotential` and `ClassOf` are in [IsPotential.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotential.lean#L84), `Mon` and `Man` in [ExistsEqAlgebraMapAddPowMul.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsEqAlgebraMapAddPowMul.lean#L230), and $Z^1_f$ in [Statement.lean](lean:Formalism/WeaklyAdmissibleFiltrations/Statement.lean#L238). We did not open the proofs of the seven lemmas.

The hypothesis $\ell \ne 2$ is not stated; the proof gets it from $\eta < H$ and $8H + 1 < \ell$ by `omega` (line 104).
