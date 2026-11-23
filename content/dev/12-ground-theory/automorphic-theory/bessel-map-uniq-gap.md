---
id: bessel-map-uniq-gap
title: Uniqueness of Bessel maps for discrete series with large gaps
kind: theorem
decl: CompanionTheory.Bmu.besselMapUniqGap
module: CompanionTheory.AutomorphicTheory.BesselOrbitBounds.BesselMapUniqueness.BesselMapUniqGapAlt
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem proves that a discrete series of a real unitary group with large gaps in its parameter has at most one Bessel map of a given type, up to a scalar. It is one of the inputs of [HypsAlt](/step/nonempty-hyps/). The [real-place integral bound](/entry/real-obj-in-infinity-x-jsz/) and other callers take it as a hypothesis. Its proof uses the [multiplicity-one theorem](/entry/thm-m/).

## Statement

Let $k \geq 1$, $r \geq 0$ and $n = 2r + k + 1$. Let $G$ be the unitary group of the hermitian form $H_{k,r}$ on $\mathbb{C}^n$: $r$ hyperbolic pairs and the diagonal form $\mathrm{diag}(1, \ldots, 1, -1)$ of size $k + 1$. Let $N \subset G$ be the unipotent subgroup `Nset`. Let $z$ be a vector in the middle block with $-H_{k,r}(z, z) > 0$, and let $W \subset G$ be the stabilizer of $z$ and of the isotropic vectors. For $c \in (\mathbb{C}^\times)^r$, let $\psi_c(m) = \exp(i \operatorname{Re} \sum_a c_a \ell_a(m))$ be the character `psiGen` of $N$.

Let $\sigma$ be a discrete series of $G$ with Harish-Chandra parameter $\lambda$ and signs $\varepsilon$. Assume that $|\lambda_a - \lambda_b| \geq h$ whenever $\varepsilon_a \neq \varepsilon_b$, with $h \geq 120 n^3$. Let $\pi$ be a representation of $W$ of the type `IsHCTypeW`. A *smooth Bessel map* is a map $B$ from the smooth vectors of $\sigma$ to the space of $\pi$ that is $\mathbb{C}$-linear, satisfies $B(\sigma(hm)v) = \psi_c(m)\pi(h)B(v)$ for $h \in W$ and $m \in N$, and is bounded by finitely many derivatives of $v$.

**Theorem.** Any two smooth Bessel maps $B_1, B_2$ are linearly dependent: there is $(a, b) \neq (0, 0)$ with $aB_1 + bB_2 = 0$ on smooth vectors.

This has the shape of a special case of the uniqueness of Bessel models at a real place (Jiang, Sun and Zhu, Geom. Funct. Anal. 20, 2010). The Lean proof does not use that paper. It uses the gap condition and square integrability.

## Proof

The proof is `uniq_of` with five proved inputs.

1. From the type of $\pi$, `stDiagExists` gives diagonal data $D$. The discrete series is square integrable.
2. The gap gives decay of matrix coefficients: $|\langle v, \sigma(x)w\rangle| \leq C\|x\|^{-4n^3}$ for smooth $v, w$. Choose a $K$-finite unit vector $w_0$.
3. The [multiplicity-one theorem](/entry/thm-m/) gives a map $l$ for the standard character $\psi_{\mathrm{std}}$ of the form `IsMultOneMap`.
4. `TorConj` gives $\tau \in G$ that commutes with $W$ and conjugates $\psi_c$ into $\psi_{\mathrm{std}}$. So $v \mapsto B_i(\sigma(\tau)v)$ is a Bessel map for $\psi_{\mathrm{std}}$.
5. `Bounded`: each such map is bounded on the orbit of $w_0$. Then `orbit_mult` gives $c_i$ with $B_i(\sigma(\tau)\sigma(x)w_0) = c_i\, l(\sigma(x)w_0)$ for all $x \in G$. It uses the reproducing formula $\int_G \overline{\langle v, \sigma(y)w_0\rangle}\, \sigma(y)w_0 \, dy = d^{-1}v$, with $d$ the formal degree.
6. If $a c_1 + b c_2 = 0$, then $aB_1 + bB_2$ vanishes on the orbit of $w_0$, so on all smooth vectors, because $w_0$ is cyclic. Take $(1, 0)$ if $c_1 = 0$, and $(c_2, -c_1)$ otherwise.

## In the Lean code

The theorem is in [BesselMapUniqGapAlt.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGapAlt.lean#L33). The statement is in [BesselMapUniqGap.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGap.lean#L252). `uniq_of` and `orbit_mult` are in [OrbitMult.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/OrbitMult.lean#L127). The inputs `Bounded`, `CutLim`, `TorConj`, `DsAd` and `Factor` come from statement theorems of `GlobalTheory.T` (Iwasawa, Levi and Cartan decompositions, derived series, root vectors). We have not unfolded those.

The same statement is defined twice: `CompanionTheory.Lime.BM.UniqGap` in [AtFormAdmOneOfSteps.lean](lean:CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/AtFormAdmOneOfSteps.lean#L15) is a copy, and `uniqGap_holds` proves it by this theorem. The character `psiGen` is also defined three times with the same body.
