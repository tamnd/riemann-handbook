---
id: exists-s-pack-integrable-alt
title: An S-pack with an integrable archimedean coefficient
kind: theorem
decl: GlobalTheory.Mem.SRe.exists_sPack_integrable_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ExistsSPackIntegrable
covers: 1867
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `PackEx`: each datum with large gaps and local ties has an S-pack whose archimedean matrix coefficient is integrable. Its only user is [the step from level three to level four](/entry/has4-of-has3-of-s-ext-none/), where it is the third of five facts. The theorem repacks the result of [`local_bessel_uniqueness_holds`](/entry/local-bessel-uniqueness-holds/). The real content is in [the spectral setting of a datum with large gaps](/entry/exists-spectral-data-gap-alt/). Below this theorem are 1,867 declarations.

## Statement

**Theorem.** Assume `SiegelWeilUnitaryConvergent` and `RowsFinDim`. Let $D$ be a datum (`D7`) and let $F$ give a form `Forms0 D u` for each word $u$. Suppose:

- `GapHyp D`: the rank satisfies $r \ge 1801$, and at each archimedean place $\tau$ the Harish-Chandra parameter $b$ of $D$ at $\tau$ satisfies $b_{j+1} - b_j \ge 16 r^{19}$ for each $j$ with $j + 1 < m$;
- `LocTied D`: at each finite place of $D$ there is a local isomorphism `LocIso` between two local data of $D$ (not unfolded).

Then there is an S-pack $P$ for $(D, F)$ such that the function $\varphi_P$ is integrable on $G_\infty$ for the measure `muInf`.

Here $\varphi_P(g) = \bigl(\prod_v d_v\bigr) \cdot \overline{\prod_v \langle w_v, \sigma_v(g_v) w_v \rangle}$. The product is over the infinite places $v$, $\sigma_v$ is the discrete series of the Hida setting at $v$, $w_v$ is its chosen vector and $d_v$ is its formal degree (`fdegOf`).

An S-pack (`SPack D F`) has these parts:

- a Hida setting $X$ for $D$: a unitary group instance whose CM field is identified with the field of $D$, with a basis, a lattice and discrete series at the infinite places; and an isomorphism of adelic groups (`AdBridgeIso`);
- a datum `Full` $Y$ over $X$ (a level character, row representatives and column systems) and the finiteness record `FinX Y`;
- an additive character $\psi$ of $\mathbb{A}_F$ with $\psi_\infty(x) = \exp\bigl(2\pi i \sum_w \operatorname{Re} x_w\bigr)$, and compatibilities of $\psi$ with the measures;
- for each word $u$ a transport: an isometry of the hermitian space of $D$ that sends the hyperbolic vectors of $X$ to those of $D$. The column dictionary of the transport maps into the right space, is bijective, matches levels and is an isometry;
- the instance of $X$ is `instOf D`, the identification of fields is the identity, and an operator record `GoodOp X`.

## Proof

`local_bessel_uniqueness_holds` gives all parts except `GoodOp X`, and gives the integrability. `rowDict_goodOp_nonempty D X` gives `GoodOp X`, with no hypothesis. The proof puts the parts into the structure. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsSPackIntegrable.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ExistsSPackIntegrable.lean#L10). `SPack` is defined in [SameDegreeZeroFormsSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SameDegreeZeroFormsSelf.lean#L17), `GapHyp` in [ConcreteSettingExists.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ConcreteSettingExists.lean#L13), and $\varphi$ in [ProjRows.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ProjRows.lean#L117).

The conclusion is the body of `PackEx` in [IwasawaDecomposition/LevelThreeToFour.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LevelThreeToFour.lean#L92). The version without `_alt`, [`exists_sPack_integrable`](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSPackIntegrable.lean#L14), has the same conclusion and one more hypothesis, `BesselMapUniq`. This version drops it.
