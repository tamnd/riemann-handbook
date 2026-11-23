---
id: exists-level-b1-carried-of-level-i-same-gal
title: A second level datum after a change of base
kind: theorem
decl: GlobalTheory.HeightCounting.Up.exists_levelB1_carried_of_levelI_same_gal
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityBoundTransferOfCmDatum
covers: 396
status: drafted
drafted_by: writer@claude
---
This theorem is the first half of [moving a third level datum to an enlarged base](/entry/multiplicity-bound-of-local-components-alt/). It makes a twisted copy of the datum of the old stage on the new side and puts a second level datum on it. It reaches that theorem through [a relay](/entry/level-i-same-gal-transfer-to-level-b1-list/).

## Statement

Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`. Then the statement `MoveToBase hL` of [the parent](/entry/multiplicity-bound-of-local-components-alt/) holds with one change: the stage $x''$ of $P'$ has a second level datum, not a third. The other two conclusions are the same: `Carried` $(D(x), D(x''))$, and `ListSt c x` implies `ListSt c x''` for every real $c$.

## Proof

Fix a column $w'$ and the data $B, w, P, x, P', x'$ of the statement.

1. `Step.of_evG` reduces the claim to one context. Two eventual facts, `hostHyp_frames_ev` and `vstd_size_ev`, give the bound $8 f r + 4 \le n_V$ and `HostHyp` for every stage family over the context.
2. `exists_eigenform_copy_of_eigensystem_alt` uses `SameGal` $(D(x), D(x'))$. It gives a new twist datum $N$ on $D(x')$ (`TwNew`), a ring map $\iota$ and a ring isomorphism $e$ with `CopyN` $(D(x), N, \iota, e)$: the datum $N$ copies the twist data of $D(x)$ along $\iota$ and $e$, field by field.
3. `twisted_state_transport_heq'` takes the intermediate level datum $l'$ of $x'$ and gives a stage $x''$ of $P'$ with an intermediate level datum $l''$. The point of $x''$ is the twist of that of $x'$ by $N$ (`oTw`), and its level characters and seven components of $l''$ are the twists or copies of those for $x'$ and $l'$. So $D(x'')$ is the datum `N.toD7`, by definition.
4. [The second level datum on the twisted copy](/entry/multiplicity-pos-of-restricted-eigenform-copy-alt/) gives a second level datum at $x''$.
5. `CopyN.carried` gives `Carried` $(D(x), N.\mathrm{toD7})$, that is `Carried` $(D(x), D(x''))$.
6. `hecke_eigenvalue_list_transfer_upper_alt` gives the list transfer.

The real content is in step 4.

## In the Lean code

The theorem is in [MultiplicityBoundTransferOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundTransferOfCmDatum.lean#L24). `CopyN` and `CopyN.carried` are in [ThetaPsi.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ThetaPsi.lean#L13), and `SameGal` and `Carried` in [ExistsUnlocalizedSaturatedState.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsUnlocalizedSaturatedState.lean#L47). We have read the statements of the lemmas of steps 2, 3 and 6, not their proofs. Step 3 is itself a relay for `restage_copy_alt`.

The name seems to say "level I" for the third level datum at $x$ and "level B1" for the second level datum of the conclusion; the code calls these `ThirdIntermediateLevel` and `SecondIntermediateLevel`. The file name speaks of a multiplicity bound and a CM datum; no multiplicity appears in the statement.
