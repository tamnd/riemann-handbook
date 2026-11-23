---
id: exists-positions-global
title: Wach-type lattices at all embeddings, glued from local ones
kind: theorem
decl: GlobalTheory.WachPlace.exists_positions_global
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSlotsGlobal
covers: 831
status: drafted
drafted_by: writer@claude
---
This theorem is step 4 of the proof of [the Wach lattices of an integral block](/entry/wach-lattices/). It gives the lattice data $N$ and $N_{\psi}$ there, together with reduced matrices that form a chain. It works one Frobenius orbit of embeddings at a time: at each orbit it goes to an unramified local field, builds the data there, and then glues the orbits.

## Statement

Keep the notation of [the parent entry](/entry/wach-lattices/): $E$ a number field, $\ell \neq 2$ prime to the discriminant of $E$, $\Phi$ the embeddings $E \to \overline{\mathbb{Q}}_\ell$, and $\sigma$ a Frobenius lift on $\Phi$. Let $L$ contain $\mu_\ell$ and all $\tau(E)$. Let $r \colon G_E \to \mathrm{GL}_n(\mathcal{O}_L)$ be crystalline with weights $J(\tau, \cdot) \subseteq [0, h]$, and let $\psi_s \colon G_E \to \mathrm{GL}_1(\mathcal{O}_L)$, $s < t$, be crystalline with weight $w_s(\tau) \in [0, h]$. Assume `BhattScholzeCrystallineLattices` and:

- a matrix form $x$ of a stable lattice chain for $r$ and $\psi$ (`GalMats.Chain`), with reduced ranks $\dim_k$ and line positions $r_s$;
- $u = 1 + \ell c$ in $\mathbb{Z}_\ell^\times$ with a series $u_n$ such that `IsUn` holds, a primitive $\ell$-th root of unity $\zeta$, and maps $j_a$ that send $X$ to $\zeta^a \exp(X) - 1$ (`IsExpAt`), for $0 < a < \ell$.

Then there are $N$ of rank $n$, $N_{\psi,s}$ of rank one, and for each $\tau \in \Phi$ a tuple $y_\tau$ of matrices over $F[[X]]$, $F$ the residue field of $L$, such that $N$ satisfies `LatN` with weights $J$, each $N_{\psi,s}$ satisfies `LatN` with weight $w_s$, and $(y_\tau, y_{\sigma\tau})$ satisfies `Slot.Chain` for every $\tau$. `Slot.Chain` says that the reduced matrices of $x$ intertwine the reduced Frobenius and $\gamma$ of $N$ and $N_\psi$ (`RedHom`), with the ranks $\dim_k$ over $F((X))$, and that the line relations of the chain hold.

## Proof

1. `HWL.exists_hw_fon_cmp_ties` turns the published input into a local Wach theory, with its frames and comparison maps. See [the local theory and its ties](/entry/exists-hw-fon-cmp-ties/). This is the only use of `BhattScholzeCrystallineLattices`.
2. Fix $\tau_0 \in \Phi$. `T.exists_unramifiedLocalSituation_of_embedding` gives an unramified extension $K$ of $\mathbb{Q}_\ell$ of degree $f$, a map $G_K \to G_E$, and an injection $\kappa \colon \mathbb{Z}/f \to \Phi$ with $\tau_0$ in its image and $\kappa(j - 1) = \sigma(\kappa(j))$. It also moves the crystalline hypotheses on $r$ and $\psi_s$ to $G_K$.
3. `exists_positions` then builds the local data over $K$. It takes Wach frames for $r$, the steps of the chain and the $\psi_s$, and reduces the matrices of the maps between them. This gives `LatAt` at each $j \in \mathbb{Z}/f$ and the chain relation between $j$ and $j - 1$.
4. `glue_orbits` is a lemma on permutations. Assume that for each $i_0$ there is an injection from a set with a permutation into $\Phi$, compatible with $\sigma$, with $i_0$ in its image, and data on that set that satisfy a relation along the permutation. Then there is data on all of $\Phi$ that satisfies the relation along $\sigma$.
5. `latN_iff` turns the pointwise `LatAt` into `LatN`.

## In the Lean code

The theorem is in [ExistsSlotsGlobal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L257). It calls:

- `exists_positions` ([L124](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L124)) and `glue_orbits` ([L207](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L207)), in the same file;
- `HWL.exists_hw_fon_cmp_ties`, `MemLoc.record_nonempty` and `T.exists_unramifiedLocalSituation_of_embedding`, a second name for `PlaceLetters.exists_place`;
- `latN_iff`, with `LatAt`, `IsExpAt`, `Slot` and `Slot.Chain`, in [RankOfMulEqOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RankOfMulEqOne.lean#L124).

The theorem does not need $E$ to be CM.
