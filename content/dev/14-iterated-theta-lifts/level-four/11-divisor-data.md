---
title: Divisor data
decls:
  - GlobalTheory.Mem.Top.DivRec.geoOver_stages
  - GlobalTheory.Mem.Top.DivRec.exists_divT
  - GlobalTheory.Mem.Top.DivRec.divEx_prov
  - GlobalTheory.Mem.Top.DivRec.divEx_of_ox
  - GlobalTheory.Mem.Top.Closing.divEx_geoCl
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Divisor data

The membership statement asks for three kinds of data at each level four object: ambient data, a theta datum and a divisor datum. The previous section gave the theta datum. In this section we build the divisor datum. It carries the geometry of the Shimura varieties of the stages, the Hermitian lattices of the row spaces, the ramification of the Hecke characters, and the logarithms of the Hecke eigenvalues at the infinite places. The result is the divisor step for the slot that [the membership statement from the construction steps](/entry/member-e-closing-alt-alt/) uses.

### The divisor datum

Let $w$ be a column datum, $Z$ a later stage of $w$, and $D = D(w, Z)$ the ambient datum. Let $L$ be the coefficient field of $D$. A level four object $l$ at $w$ and $Z$ has a rows datum, a choice of characters with a tied tuple of Hecke characters $\xi$, and a reading of the true rows.

**Definition 1.11.1 (Divisor datum).** A divisor datum $Y$ over $D$ consists of the following.

1. Geometry: a level type, Shimura data at each level, components with their curves and surfaces, and the places of $L$ over each prime with their weights.
2. Lattices: for each $j$ a Hermitian lattice $M_j$ (see [lattices in quadratic and Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces)) with an isometry onto the space $M_j$ of $D$.
3. Ramification: for each tuple $\mu$ a finite set $Q_p(\mu)$ of primes, a finite set of places and local values at these places.
4. Eigenvalues: real numbers $\log \lambda(j, \sigma, e)$ for each degree $j$, each class $\sigma$ and each complex embedding $e$ of $L$, and constants $\kappa_R(\sigma)$.

The datum $Y$ is tied to the choice of characters of $l$ if $Q_p(\mu)$ is the set of primes under the primes of the column at $\mu$, the ramification data match the character tuple $\xi$, the local data are tied at each selected place, and there is a family of Shimura varieties to which the geometry of $Y$ is tied. The lattices are tied to the reading of $l$ if each $M_j$ is the lattice of the reading. The eigenvalues are tied if each $\sigma$ has a label $c$ and, for each embedding $e$ other than the base embedding, $\log\lambda(i+1, \sigma, e)$ is the logarithm of the eigenvalue $\lambda_i(\mu_0, c)$ at the infinite place of $e$ when the isotypic part of $\sigma$ in degree $i+1$ is nonzero, and $0$ otherwise.

The geometry part says where the divisors of the construction live. The other three parts are read off the stage: the lattices from the rows, the ramification from the characters, the eigenvalues from the Hecke action at infinity.

**Definition 1.11.2 (Geometry over a datum).** Let $Q$ be a property of divisor data and $X_0$ a divisor datum over $D$. A datum $X$ has geometry over $X_0$ with $Q$ if $X$ keeps $X_0$ (it has the lattices, the ramification, the eigenvalues and the constants of $X_0$, and its geometry is grafted onto them), if the geometry of $X$ is tied to a family of Shimura varieties, and if $Q(X)$ holds.

**Lemma 1.11.3 (Geometry over the stages).** Let $X$ be the stages of a construction and $X_0$ a divisor datum over its ambient datum. Then there is a divisor datum with geometry over $X_0$, for the property that always holds.

Lean: `GlobalTheory.Mem.Top.DivRec.geoOver_stages`.

*Proof.* For each prime $p$ and each place of $L$ over $p$, choose a complex embedding of the Witt fraction field that is pinned to the place. These embeddings are compatible. The flat datum built from them and $X_0$ has a family of Shimura varieties over the field $K_s$ of the base, with identity maps on the places, and the flat datum is tied to this family. Its level maps are inverse to each other and it is tied in each level. Graft its geometry onto $X_0$. $\square$

### Existence of the divisor datum

**Theorem 1.11.4 (Divisor datum of a level four object).** Let $w$ be a column datum with a pin, $Z$ a later stage, and $l$ a level four object of a slot at $w$ and $Z$. Then there is a divisor datum $Y$ over $D(w, Z)$ that is tied to the choice of characters of $l$, whose lattices and eigenvalues are tied to the reading of $l$, and with $\kappa_R(\sigma) = \kappa^\sharp(D)$ for all $\sigma$.

Lean: `GlobalTheory.Mem.Top.DivRec.exists_divT`.

*Proof.* Step 1 (Pins of the tuple). From the rows datum of $l$, the character tuple $\xi$ has pins. Where a character $\xi_\mu$ ramifies at a place $v$, the place $v$ is split, it has prime norm $p$, it is unramified over $p$, and it is not over the auxiliary primes. For each place $w$, the character of $w$ is unramified at the places over the residue characteristic of $w$.

Step 2 (First datum). Build a datum $X_1$ with empty geometry and empty ramification, with the lattices of the reading, with $\log\lambda$ the logarithms of the eigenvalues of the reading, and with $\kappa_R = \kappa^\sharp$.

Step 3 (Ramification). Replace the ramification of $X_1$ by the sets that the pins of step 1 and the selected places of the pin of $w$ give. Call the result $X_2$. The reduced divisor character gives the compatibility of $X_2$ with $\xi$, and the local reading gives the tie at each selected place.

Step 4 (Geometry). The lemma on geometry over the stages, applied to $X_2$, gives a datum $Y$ with geometry over $X_2$. So $Y$ keeps the lattices, the ramification, the eigenvalues and $\kappa_R$ of $X_2$, and its geometry is tied to a family of Shimura varieties.

Then the prime sets of $Y$ are those of the column, by the pins of step 1. The lattices are tied by the existence of Hermitian ties for the lattices of the reading. The constants are $\kappa^\sharp$ and the eigenvalues are tied, since $Y$ keeps them from $X_1$. $\square$

A slot has four components: a position, a norm condition, a side position and an object component. The object component says which property an object over a divisor datum must have. The object component of geometry $\Gamma$ asks for an object over $Y$ that has $\Gamma$ and whose eigenvalues are tied to the reading. The divisor step for a slot is a column step from "pinned" to: each level four object $l$ has a divisor datum $Y$ as in the theorem, and each object over $Y$ with the base row side and the rows datum of $l$ satisfies the object component.

**Corollary 1.11.5 (The divisor step).** Let $\mathcal{S}$ be a slot whose object component is the object component of the geometry that always holds. Then the divisor step holds for $\mathcal{S}$.

Lean: `GlobalTheory.Mem.Top.DivRec.divEx_prov` (also `GlobalTheory.Mem.Top.DivRec.divEx_of_ox`, the same result with three more hypotheses that it does not use).

*Proof.* Fix a pinned column datum $w$, a stage $Z$ and a level four object $l$. The theorem on the divisor datum gives $Y$. Let $O$ be an object over $Y$ whose base row side and rows datum are those of $l$. The geometric condition holds always. The eigenvalue tie of $Y$ for the reading of $l$ is the eigenvalue tie for the rows datum of $O$, since the two rows data are equal. $\square$

The membership statement uses the closure of a geometric property. The closure of $\Gamma$ is the smallest property that contains $\Gamma$ and that is stable under the step that replaces the divisor of $D$, the core and the divisor datum together.

**Theorem 1.11.6 (The divisor step for the closed geometry).** Assume the existence of ray class fields, the principal ideal statement and good reduction of CM curves outside a prime, as in [Section 1.8.8](/entry/member-e-of-steps2/). Let $\mathcal{S}$ be a slot whose object component is the object component of the closure of the geometry that always holds. Then the divisor step holds for $\mathcal{S}$.

Lean: `GlobalTheory.Mem.Top.Closing.divEx_geoCl`.

*Proof.* Let $\mathcal{S}_0$ be the slot with the same position, norm condition and side position, and with the object component of the geometry that always holds. The divisor step holds for $\mathcal{S}_0$ by the corollary. A level four object of $\mathcal{S}$ is a level four object of $\mathcal{S}_0$ with the same data, so it has a divisor datum $Y$. An object over $Y$ that has the geometry that always holds also has its closure, since the closure contains the property. $\square$

**Remark 1.11.7 (Formalization).** The three literature hypotheses `RayField`, `PrincipalIdealSt` and `CMCurveGoodOutsidePrimeSt` are discarded in [TupPinsOfMuIsW.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L211); the divisor step for the closed geometry holds without them. The property `anyGeometry` is the constant `True` ([OverIx.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19)), so its closure is also always true, and the geometric part of the object component is empty. The lemma `geoOver_stages` ([TupPinsOfMuIsW.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L155)) uses the property `True`, and the flat datum `divXFl` is not unfolded here. The label of $\sigma$ (`labOf`, line 35) is a choice with an arbitrary fallback when no index fits. The lemmas `mjAre_x0` (line 174) and `lamAre_x0` (line 194) are not used. The pin in `divEx_prov` (line 204) is used only to choose a pin of $w$.
