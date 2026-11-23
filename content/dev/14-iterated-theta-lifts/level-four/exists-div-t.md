---
id: exists-div-t
title: A divisor datum for a level-four record
kind: theorem
decl: GlobalTheory.Mem.Top.DivRec.exists_divT
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.TupPinsOfMuIsW
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem builds the divisor datum of the divisor step. Its only caller is [`divEx_prov`](/entry/div-ex-prov/), which adds the trivial geometric condition.

## Statement

Let $w$ be a column datum over a base $B$, with a pin (`ColPin w`), let $Z$ be a later stage of $w$, and let $l$ be a level-four record (`Lv4`) at $w$ and $Z$ for some slots $\mathcal S$. Write $D = w.D(Z)$.

A *divisor datum* over $D$ (`DivX D`) is a large record. Its fields, grouped:

- geometry: a geometric datum, a level type, Shimura data for each level, components with curves, surfaces, and the places of the field $L = D.\mathrm{LL}$ over each prime, with weights;
- lattices: for each $j$, a hermitian lattice $M_j$ with an isometry $j_M$ onto the space $D.M_j$ that matches the lattice of $D$;
- ramification: for each tuple $\mu$, a finite set $Q_p(\mu)$ of primes, a finite set of places, and local values at each place;
- eigenvalues: real numbers $\log\lambda(j, \sigma, e)$ for each complex embedding $e$ of $L$, and constants $\kappa_R(\sigma)$.

**Theorem.** There is a divisor datum $Y$ over $D$ such that:

1. `DivT` holds for the character choice of $l$: $Q_p(a)$ is the set of primes under the primes `I.Q a` of the column; the ramification data of $Y$ match the character tuple of $l$; at each selected place the local data are tied (`QLocTiedC`); and there is a family of Shimura varieties to which $Y$ is tied (`GeoTiedP`);
2. `MjAre`: the lattices $M_j$ are tied to the reading of $l$;
3. $\kappa_R(\sigma) = \kappa^\sharp(D)$ for all $\sigma$;
4. `LamAre`: each $\sigma$ has a label $c$; for $e$ not the base embedding, $\log\lambda(i+1, \sigma, e)$ is the logarithm of the eigenvalue $\lambda_i(\mu_0, c)$ at the infinite place of $e$ when the isotypic part of $\sigma$ in degree $i+1$ is nonzero, and $0$ when it is zero.

## Proof

1. `tupPins_of_muIsW` proves `TupPins` for the character tuple of $l$, from the field `mu` of the rows record. It says: where a character $\xi_\mu$ ramifies at $v$, the place $v$ is split, has prime norm $p$, is unramified over $p$, and is not over the primes $g_k$; and for each place $w$, the character $\xi_{\mu(w)}$ is unramified at the places over the residue characteristic of $w$.
2. `x0` builds a first datum $X_1$ with empty geometric and ramification fields, lattices from the reading, eigenvalues `logLamOf`, and $\kappa_R = \kappa^\sharp$.
3. `ReQ.reQ` replaces the ramification fields of $X_1$, with the pins of step 1 and the selected places of the pin. The result is $X_2$. `reducedDivisorCharacter` and `reLoc` give the character compatibility and the local tie. The local values come from lemmas that we have not opened.
4. `geoOver_stages` gives a datum $X_g$ (`divXFl`, not unfolded) and maps $i_M$ such that $Y = $ `graft` $X_g\, X_2$ is tied to a Shimura family. `graft` takes the geometry from $X_g$ and keeps the lattices, ramification, eigenvalues and $\kappa_R$ of $X_2$.

Then `qpIs_qpSet` gives the prime set clause, `exists_mjHTie` gives `MjAre`, $\kappa_R$ holds by `rfl`, and `lamAre_of_eq` gives `LamAre` because $Y$ keeps `logLamOf`.

## In the Lean code

The theorem is in [TupPinsOfMuIsW.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L178). `DivX` is in [DataDIV.lean](lean:Formalism/LocalRingCardinality/DataDIV.lean#L418) and `DivT` in [TiedColumnData.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TiedColumnData.lean#L127).

The label of $\sigma$ (`labOf`) is chosen by `Classical.choose`, and is an arbitrary index when no index satisfies `OverIx`. The lemmas `mjAre_x0` and `lamAre_x0` of the same file are not used here.
