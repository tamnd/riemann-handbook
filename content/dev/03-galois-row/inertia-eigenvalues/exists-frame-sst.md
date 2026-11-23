---
id: exists-frame-sst
title: A Breuil-Kisin frame for a semistable lattice with bounded jumps
kind: theorem
decl: GlobalTheory.BKLim.exists_frame_sst
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsBreuilKisinFrameSemistableBoundedJumps
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem attaches a Breuil-Kisin frame of height $N$ to a lattice in a semistable representation with Hodge-Tate jumps in $[-N, N]$. Through its second name [exists_breuilKisinFrame_semistable_boundedJumps](/entry/exists-breuil-kisin-frame-semistable-bounded-jumps/) it serves the arguments on towers of lattices below [coreAll_of](/entry/core-all-of/). The proof builds a frame of some height from period matrices and then lowers the height to $N$. Below it are 350 declarations.

## Statement

Fix a prime $\ell$ and a finite extension $K/\mathbb{Q}_\ell$. Let $\mathfrak{S} = W[[u]]$ with $W = W(\mathbb{F}_{\ell^a})$.

- `bk : BK K` is a Breuil-Kisin datum: an Eisenstein polynomial $E \in W[u]$, an isomorphism $\mathcal{O}_K \cong \mathfrak{S}/(E)$, and a Frobenius-compatible map $\mathfrak{S} \to A_{\inf}$ with $u \mapsto [\varpi^\flat]$, such that $E$ maps to a generator of $\ker \theta$.
- `bk.IsPer τ` says $\varphi(\tau) = E \tau$ and $\varphi(\tau) = \eta ([\varepsilon] - 1)$ for a unit $\eta$ and an $\varepsilon$ with $\varepsilon^\sharp = 1$ and an $\ell$-th root $\delta$ with $\delta^\sharp \neq 1$.
- `P`, `AI`, `T` are data of period rings. `T` ties the rings of `P` to $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$.

Let $\rho \colon G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be continuous and $V = \rho \otimes \mathbb{Q}_\ell$. Assume that $V$ is semistable ($\dim D_{\mathrm{st}}(V) = [K_0 : \mathbb{Q}_\ell] \, d$), that $D_{\mathrm{dR}}(V) \subseteq \mathrm{Fil}^{-N}(V \otimes B_{\mathrm{dR}})$, and that $D_{\mathrm{dR}}(V) \cap \mathrm{Fil}^{N+1}(V \otimes B_{\mathrm{dR}}) = 0$.

**Theorem.** There is a frame $F$ of height $N$ for $\rho$ with `F.IsDR`, and with `F.IsCr` if $V$ is crystalline.

A frame (`Frame bk N d ρ`) is an invertible matrix $T$ over $W(\mathbb{C}_\ell^\flat)$, matrices $A, A'$ over $\mathfrak{S}$ with $A A' = E^{2N}$, and a map $\varepsilon \colon G_K \to M_d(A_{\inf})$ such that $E^N \varphi(T) = T A$, $\rho(g) \, g(T) = T$ for $g$ that fix $\varpi^\flat$, and $\rho(g) \, g(T) = T \varepsilon(g)$ for all $g$. `IsDR` says: for each $m$ there are $k$ and $\beta$ over $\mathfrak{S}$ with $\beta \equiv \ell^k \bmod E$ and $\varphi(\varepsilon(g)) \, g(\beta) \equiv \beta \bmod E^m$ for all $g$. `IsCr` says $\varepsilon(g) \equiv 1 \bmod [\varpi^\flat]$.

The statement has the shape of Kisin's theorem that a lattice in a semistable representation comes from a Breuil-Kisin module of bounded height (M. Kisin, Crystalline representations and F-crystals, in Algebraic Geometry and Number Theory, Progr. Math. 253, 2006). We do not claim that they match in detail.

## Proof

1. `exists_fits` and `fits_inv` give a core `C` of period rings that fits `T`.
2. `sst_isDR`: $V$ is de Rham. Then `exists_hodge_basis_deRham_lattice` gives a Hodge datum `H` for $\rho$, and the jump hypothesis bounds its jumps by $N$.
3. A weak seed `s : WSeed`: period matrices with a cocycle $\kappa$. If $V$ is crystalline, `crys_seed` (line 102, on the standard lattice $\mathbb{Z}_\ell^d$) and `exists_trivial_cocycle_crystalline_period_data` give one with $\kappa = 1$. If not, `exists_semistable_lattice_periods_acris` and `semistableSeed_of_acris_periods` make one from period matrices over $A_{\mathrm{cris}}$.
4. `exists_breuilKisinFrame_semistablePeriods` turns `s` into a frame of some height $N'$, de Rham, and crystalline when $\kappa = 1$.
5. `exists_breuilKisin_frame_height_of_jumps_le` uses `H` to give a frame of height $N$ with the same $T$ and $\varepsilon$. `IsDR` and `IsCr` depend only on $\varepsilon$, so they carry over. We have not opened the proofs of the lemmas in steps 2 to 5.

## In the Lean code

The theorem is in [ExistsBreuilKisinFrameSemistableBoundedJumps.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinFrameSemistableBoundedJumps.lean#L109). `Frame`, `IsDR`, `IsCr` and `WSeed` are in [TrivIsCr.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TrivIsCr.lean#L67), `BK` and `IsPer` in [IsStratHom.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsStratHom.lean#L14), and $D_{\mathrm{dR}}$ and the filtration in [Statement.lean](lean:Formalism/WeaklyAdmissibleFiltrations/Statement.lean#L134).

Continuity of $\rho$ is used only in the crystalline case. In the other case, "crystalline implies `IsCr`" holds by contradiction.
