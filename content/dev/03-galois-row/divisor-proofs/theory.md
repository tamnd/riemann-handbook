---
id: theory
title: A Dieudonné theory for p-divisible groups over perfect fields
kind: definition
decl: GlobalTheory.Dieu.theory
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankTheoryMu
covers: 371
status: drafted
drafted_by: writer@claude
---
This definition picks one Dieudonné theory for each prime $p$: a contravariant functor from $p$-divisible groups over perfect fields of characteristic $p$ to free modules over the Witt vectors, with Frobenius, Verschiebung and a reduction to rigidified extensions. It is built by choice from four existence theorems. [The proof in characteristic p](/entry/charpoly-push/) uses it to compute characteristic polynomials on de Rham homology.

## Statement

Fix a prime $p$. For a perfect field $k$ of characteristic $p$ write $W = W(k)$. A *base* (the Lean structure `Dieu.Base`) for a class of $p$-divisible groups consists of:

- **The functor.** A $W$-module $M(G)$ for each $G$ in the class, free of finite rank. For a ring map $\sigma \colon k \to k'$ and a morphism $s$ from $G'$ to $G$ over $\sigma$, an additive map $M(G) \to M(G')$, $\sigma$-semilinear for $W(\sigma)$. These maps respect identities, sums and composition.
- **The reduction.** A surjective map $\mathrm{red} \colon M(G) \to \operatorname{RigExt}(G)$, semilinear over $W \to k$, with kernel $pM(G)$, and compatible with the maps above. $\operatorname{RigExt}(G)$ is a $k$-space of classes of pairs (a 2-cocycle, an invariant differential), see [the proof in characteristic p](/entry/charpoly-push/).

From a base one defines $F \colon M(G) \to M(G)$ as $M$ of the absolute Frobenius; it is semilinear for the Frobenius of $W$.

A *theory* (`Dieu.Theory`) is a base on all $p$-divisible groups with:

- `katz`: for $G$ with a chart that makes it a formal group law $\mu$, an isomorphism of $M(G)$ with a module `Katz.Mod p μ` built from $\mu$, that matches $F$ and the maps of $M$ with the ones on the side of $\mu$;
- `etDual`: for étale $G$, a pairing $M(G) \cong \operatorname{Hom}_W(M(G^\vee), W)$ with $\langle Fx, Fy \rangle = p\,\mathrm{Frob}\langle x, y \rangle$, natural in $G$;
- a map $V$, semilinear for the inverse Frobenius, with $FV = VF = p$.

**Definition.** `Dieu.theory p` is the theory whose fields are chosen witnesses of:

1. `T.exists_connected_dieudonne_functor_quasiLogarithms`: a base $B_c$ on connected groups with `katz`;
2. `T.exists_etaleDieudonneBase_by_cartierDuality`: from $B_c$, a base $B_e$ on étale groups, dual to $B_c$ by Cartier duality;
3. `T.exists_dieudonneFunctor_glued_connected_etale`: a base on all groups, glued from $B_c$ and $B_e$, with `katz` and `etDual`;
4. `T.exists_verschiebung_of_dieudonneFunctorBase`: the map $V$ on that base.

## Proof: why this definition

The structure `Theory` lists the properties that the proof needs. The definition makes one choice of it, so that later results can name a single Dieudonné module. [The proof in characteristic p](/entry/charpoly-push/) uses freeness, finiteness and the reduction to $\operatorname{RigExt}$, and through `Dieu.CharpolyAV.charpoly_map_eq` it uses $F$ and $V$.

## In the Lean code

The definition is in [FinrankTheoryMu.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FinrankTheoryMu.lean#L16). The structures `Base`, `Theory`, `Base.Katz` and `Base.EtDual` are in [RedSurjective.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RedSurjective.lean#L38). Each of the four theorems is an alias: of `exists_base_isConn_katz`, `dieuBase_isEt_of_isConn`, `Dieu.Glue.exists_katz_etDual` and `Dieu.exists_V_of_base`. We have not opened these, and we have not unfolded `Katz.Mod` or `KatzF.IsF`. The definition is noncomputable, by `Exists.choose`. The file name says `FinrankTheoryMu`; the file holds only this definition.
